import sqlite3
import random

DB_PATH = "flashcards.db"

def init_db():
    """Initialize the database. Creates the flashcards table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        """)
    conn.commit()
    conn.close()
    
def add_flashcard(user_id, question, answer):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flashcards (user_id, question, answer) VALUES (?, ?, ?)", (user_id, question, answer))
    conn.commit()
    conn.close()
    

def get_flashcards(user_id):
    """Fetch all flashcards for a given user."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, answer FROM flashcards WHERE user_id = ?", (user_id,))
    cards = cursor.fetchall()
    conn.close()
    return cards


def get_random_flashcard(user_id):
    """Return one random flashcard for the user."""
    cards = get_flashcards(user_id)
    if not cards:
        return None
    return random.choice(cards)