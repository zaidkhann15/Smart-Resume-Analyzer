from nltk.tokenize import word_tokenize

roles = {

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "tableau",
        "power bi",
        "statistics",
        "pandas"
    ],

    "Data Scientist": [
        "python",
        "machine learning",
        "tensorflow",
        "numpy",
        "sql",
        "pandas",
        "scikit-learn"
    ],

    "AI Engineer": [
        "python",
        "deep learning",
        "tensorflow",
        "pytorch",
        "nlp",
        "machine learning"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "bootstrap"
    ],

    "Cloud Engineer": [
        "aws",
        "azure",
        "docker",
        "kubernetes",
        "linux",
        "terraform"
    ]
}


def ats_score(text, role):

    text = text.lower()

    tokens = word_tokenize(text)

    required_skills = roles[role]

    matched_skills = []

    for skill in required_skills:

        skill_words = skill.lower().split()

        if len(skill_words) == 1:

            if skill_words[0] in tokens:
                matched_skills.append(skill)

        else:

            if skill.lower() in text:
                matched_skills.append(skill)

    score = int(
        len(matched_skills)
        / len(required_skills)
        * 100
    )

    missing_skills = list(
        set(required_skills) - set(matched_skills)
    )

    return score, matched_skills, missing_skills