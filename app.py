import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text

from analyzer.scorer import calculate_resume_score
from analyzer.ats_checker import ats_score
from analyzer.feedback import generate_feedback

from database.db import conn
from database.db import cursor

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("📄 Smart Resume Analyzer")
st.write("AI Based Resume Analysis System")

# -----------------------------
# ROLE SELECTION
# -----------------------------
role = st.selectbox(
    "Select Target Job Role",
    [
        "Data Analyst",
        "Data Scientist",
        "AI Engineer",
        "Web Developer",
        "Cloud Engineer"
    ]
)

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

# -----------------------------
# PROCESS RESUME
# -----------------------------
if uploaded_file is not None:

    # Extract Text
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_pdf_text(uploaded_file)

    else:
        resume_text = extract_docx_text(uploaded_file)

    # Resume Score
    resume_score = calculate_resume_score(
        resume_text
    )

    # ATS Analysis
    ats_result, matched, missing = ats_score(
        resume_text,
        role
    )

    # Feedback
    feedback = generate_feedback(
        resume_score,
        ats_result,
        missing,
        resume_text
    )
    
    from datetime import datetime

    cursor.execute(
    """
    INSERT INTO resumes(
        file_name,
        role,
        resume_score,
        ats_score,
        upload_date
    )
    VALUES (?,?,?,?,?)
    """,
    (
        uploaded_file.name,
        role,
        resume_score,
        ats_result,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    )

    conn.commit()

    # Resume Rating
    if resume_score >= 90:
        rating = "Excellent ⭐⭐⭐⭐⭐"

    elif resume_score >= 70:
        rating = "Good ⭐⭐⭐⭐"

    elif resume_score >= 50:
        rating = "Average ⭐⭐⭐"

    else:
        rating = "Needs Improvement ⭐⭐"

    st.success(
        "Resume analyzed successfully!"
    )

    st.subheader(
        f"Resume Rating: {rating}"
    )

    # -----------------------------
    # SCORE CARDS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Resume Score",
            f"{resume_score}/100"
        )

    with col2:
        st.metric(
            "ATS Score",
            f"{ats_result}%"
        )

    # -----------------------------
    # ATS STATUS
    # -----------------------------
    if ats_result >= 80:

        st.success(
            "✅ ATS Friendly Resume"
        )

    elif ats_result >= 60:

        st.warning(
            "⚠ Moderately ATS Friendly"
        )

    else:

        st.error(
            "❌ Needs ATS Improvement"
        )

    # -----------------------------
    # SUMMARY CARD
    # -----------------------------
    st.info(
        f"""
    Resume Score: {resume_score}/100

    ATS Score: {ats_result}%

    Matched Skills: {len(matched)}

    Missing Skills: {len(missing)}
    """
        )

    # -----------------------------
    # CHARTS SIDE BY SIDE
    # -----------------------------
    chart1, chart2 = st.columns(2)

    with chart1:

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=ats_result,
                number={"font": {"size": 40}},
                title={"text": "ATS Compatibility"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "green"}
                }
            )
        )

        fig.update_layout(
            height=320,
            margin=dict(l=20, r=20, t=50, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart2:

        df = pd.DataFrame({
            "Category": [
                "Matched Skills",
                "Missing Skills"
            ],
            "Count": [
                len(matched),
                len(missing)
            ]
        })

        fig2 = px.pie(
            df,
            names="Category",
            values="Count",
            hole=0.5,
            title="Skill Match Analysis"
        )

        fig2.update_layout(
            height=320,
            margin=dict(l=20, r=20, t=50, b=20)
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # -----------------------------
    # MATCHED SKILLS
    # -----------------------------
    st.subheader(
        "✅ Matched Skills"
    )

    if matched:

        cols = st.columns(3)

        for i, skill in enumerate(matched):
            cols[i % 3].success(
                f"✓ {skill}"
            )

    else:

        st.warning(
            "No skills matched"
        )

    # -----------------------------
    # MISSING SKILLS
    # -----------------------------
    st.subheader(
        "❌ Missing Skills"
    )

    if missing:

        cols = st.columns(3)

        for i, skill in enumerate(missing):
            cols[i % 3].error(
                f"✗ {skill}"
            )

    else:

        st.success(
            "No missing skills"
        )

    # -----------------------------
    # SUGGESTIONS
    # -----------------------------
    st.subheader(
        "💡 Suggestions"
    )

    for item in feedback:
        st.warning(item)

    # -----------------------------
    # RESUME PREVIEW
    # -----------------------------
    st.subheader(
        "📄 Resume Preview"
    )

    with st.expander("📄 View Resume Text"):
        st.text(resume_text[:3000])
    
    # -----------------------------
    # ANALYSIS HISTORY
    # -----------------------------
    col1, col2 = st.columns([5,1])

    with col1:
        st.subheader("📊 Analysis History")

    with col2:
        if st.button("🗑️ Clear"):
            cursor.execute("DELETE FROM resumes")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='resumes'")
            conn.commit()
            st.rerun()

        history = pd.read_sql_query(
        "SELECT * FROM resumes ORDER BY id DESC",
        conn
    )

    st.dataframe(
        history,
        use_container_width=True
    )
    
    report = f"""
    SMART RESUME ANALYZER REPORT

    File Name:
    {uploaded_file.name}

    Target Role:
    {role}

    Resume Score:
    {resume_score}/100

    ATS Score:
    {ats_result}%

    Matched Skills:
    {matched}

    Missing Skills:
    {missing}

    Suggestions:
    {feedback}
    """

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )
    
    st.markdown("---")
    st.markdown(
        """
        <center>
        Smart Resume Analyzer | AI Capstone Project<br>
        Developed using Python, Streamlit, SQLite and NLP
        </center>
        """,
        unsafe_allow_html=True
    )