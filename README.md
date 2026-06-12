# 📄 Smart Resume Analyzer

An AI-powered Resume Analysis System built using Python, Streamlit, SQLite, and NLP techniques.

The application analyzes resumes, calculates Resume Score and ATS Score, identifies matched and missing skills for different job roles, provides improvement suggestions, and stores analysis history in a database.

---

## 🚀 Features

### 📂 Resume Upload
- Upload resumes in PDF or DOCX format.
- Automatic text extraction.

### 📊 Resume Score Analysis
- Evaluates resume quality based on:
  - Education
  - Skills
  - Projects
  - Experience
  - Certifications
  - Resume Content Length

### 🎯 ATS Score Analysis
- Calculates ATS compatibility for selected job roles:
  - Data Analyst
  - Data Scientist
  - AI Engineer
  - Web Developer
  - Cloud Engineer

### ✅ Skill Matching
- Displays matched skills.
- Highlights missing skills.

### 💡 Smart Suggestions
- Recommends skills and improvements to increase ATS score.

### 📈 Interactive Visualizations
- ATS Compatibility Gauge Chart
- Skill Match Pie Chart

### 📄 Resume Preview
- Displays extracted resume content.

### 🗄 Database Integration
- Stores all resume analysis records.
- Maintains analysis history with timestamps.
- Option to clear analysis history.

### 📥 Report Generation
- Download resume analysis report.

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- SQLite

### Data Processing
- Pandas

### NLP
- NLTK

### Visualization
- Plotly

### Document Parsing
- PyPDF2
- python-docx

---

## 📂 Project Structure

```
Smart-Resume-Analyzer/
│
├── app.py
│
├── analyzer/
│   ├── ats_checker.py
│   ├── scorer.py
│   └── feedback.py
│
├── parser/
│   ├── pdf_parser.py
│   └── docx_parser.py
│
├── database/
│   └── db.py
│
├── requirements.txt
├── README.md
└── resume.db
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Resume-Analyzer.git

cd Smart-Resume-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Dashboard

<img width="1919" height="808" alt="image" src="https://github.com/user-attachments/assets/b3c5db34-2d2e-4395-b66c-e99d0489d2dd" />


### ATS Analysis

<img width="1919" height="963" alt="image" src="https://github.com/user-attachments/assets/f529ec5e-ac12-492b-a381-e3fe309fa7f7" />

<img width="1919" height="855" alt="image" src="https://github.com/user-attachments/assets/1814ee25-f7f3-49e3-8032-fb03258c1aa5" />


### Resume Preview

<img width="1917" height="968" alt="image" src="https://github.com/user-attachments/assets/1ea7c901-dd36-4934-a7b3-a624b71153f2" />


---

## 📊 ATS Score Calculation

The ATS score is calculated by matching resume skills against required skills for a selected role.

Example:

Data Analyst Skills:

- Python
- SQL
- Excel
- Tableau
- Power BI
- Statistics
- Pandas

If the resume contains:

- Python
- SQL
- Pandas

ATS Score:

```
3 / 7 × 100 = 42%
```

---

## 📈 Resume Score Calculation

Resume score is based on the presence of key sections:

- Education
- Skills
- Projects
- Experience
- Certifications

Additional points are awarded for sufficient content length.

---

## 🎯 Future Enhancements

- AI-powered resume recommendations
- Resume ranking system
- Job description matching
- Resume keyword optimization
- PDF report generation
- User authentication

---

## 👨‍💻 Author

**Zaid Khan**

BE Artificial Intelligence and Data Science

East Point College of Engineering and Technology

---

## 📜 License

This project is developed for academic and learning purposes.
