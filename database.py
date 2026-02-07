import sqlite3

DB_NAME = "help.db"

def setup_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        question TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_question(user_id, username, question):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO questions (user_id, username, question) VALUES (?, ?, ?)",
        (user_id, username, question)
    )

    conn.commit()
    conn.close()
