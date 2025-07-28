import sqlite3

def create_connection():
    """Create a database connection"""
    conn = sqlite3.connect('entries.db')
    return conn

def create_table():
    """Create the entries table if it doesn't exist"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
           CREATE TABLE IF NOT EXISTS entries (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT,
               journal TEXT,
               intention TEXT,
               dream TEXT,
               priorities TEXT,
               reflection TEXT,
               strategy TEXT
           )
       ''')
    conn.commit()
    conn.close()

def save_entry(date, journal, intention, dream, priorities, reflection, strategy):
    """Save a new entry to the database"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
           INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy)
           VALUES (?, ?, ?, ?, ?, ?, ?)
       ''', (date, journal, intention, dream, priorities, reflection, strategy))
    conn.commit()
    conn.close()

def get_entries_by_date(date):
    """Get all entries for a specific date"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries WHERE date = ?', (date,))
    entries = cursor.fetchall()
    conn.close()
    return entries
   