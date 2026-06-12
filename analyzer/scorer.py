def calculate_resume_score(text):

    score = 0

    sections = [
        "education",
        "skills",
        "project",
        "experience",
        "certification"
    ]

    text = text.lower()

    for section in sections:
        if section in text:
            score += 18

    if len(text) > 500:
        score += 10

    return min(score, 100)