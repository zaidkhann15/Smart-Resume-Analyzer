import sqlite3

conn = sqlite3.connect(
    "resume.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT,
    role TEXT,
    resume_score INTEGER,
    ats_score INTEGER,
    upload_date TEXT
)
""")

conn.commit()