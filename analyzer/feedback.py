def generate_feedback(
    resume_score,
    ats_score,
    missing_skills,
    resume_text
):

    feedback = []

    text = resume_text.lower()

    # ATS feedback
    if ats_score < 70:
        feedback.append(
            "Improve ATS compatibility by adding relevant keywords."
        )

    # Project check
    if "project" not in text:
        feedback.append(
            "Add technical projects."
        )

    # Certification check
    if "certification" not in text:
        feedback.append(
            "Include certifications."
        )

    # Experience check
    if (
        "experience" not in text and
        "internship" not in text
    ):
        feedback.append(
            "Add internship or work experience."
        )

    # Missing skills
    for skill in missing_skills:
        feedback.append(
            f"Add skill: {skill}"
        )

    if len(feedback) == 0:
        feedback.append(
            "Excellent Resume! Keep it updated."
        )

    return feedback