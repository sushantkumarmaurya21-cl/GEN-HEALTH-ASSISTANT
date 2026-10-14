import sqlite3
import datetime
from pathlib import Path
from backend.app.config import settings

def get_connection():
    conn = sqlite3.connect(str(settings.DATABASE_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Wellness records table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wellness_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_date TEXT UNIQUE NOT NULL,
            water_ml INTEGER DEFAULT 0,
            sleep_hours REAL DEFAULT 0.0,
            sleep_quality TEXT DEFAULT 'Normal',
            steps INTEGER DEFAULT 0,
            active_minutes INTEGER DEFAULT 0,
            calories_burned INTEGER DEFAULT 0,
            notes TEXT DEFAULT '',
            updated_at TEXT NOT NULL
        )
    """)
    
    # 2. Chat history table (session-based)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            language TEXT DEFAULT 'en',
            is_demo INTEGER DEFAULT 0,
            created_at TEXT NOT NULL
        )
    """)
    
    # 3. User settings / profile
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            display_name TEXT DEFAULT 'User',
            water_goal_ml INTEGER DEFAULT 2500,
            sleep_goal_hours REAL DEFAULT 8.0,
            steps_goal INTEGER DEFAULT 8000,
            preferred_language TEXT DEFAULT 'en',
            updated_at TEXT NOT NULL
        )
    """)
    
    # Seed default user profile if not exists
    cursor.execute("SELECT COUNT(*) as count FROM user_profile WHERE id = 1")
    if cursor.fetchone()["count"] == 0:
        now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
        cursor.execute("""
            INSERT INTO user_profile (id, display_name, water_goal_ml, sleep_goal_hours, steps_goal, preferred_language, updated_at)
            VALUES (1, 'Healthy User', 2500, 8.0, 8000, 'en', ?)
        """, (now_iso,))
        
    # Seed 7-day realistic demo wellness data if table is empty
    cursor.execute("SELECT COUNT(*) as count FROM wellness_records")
    if cursor.fetchone()["count"] == 0:
        today = datetime.date.today()
        sample_data = [
            (6, 2100, 7.5, 'Good', 7420, 35, 310, 'Felt energetic after morning brisk walk'),
            (5, 1800, 6.5, 'Fair', 5890, 20, 240, 'Busy day at work'),
            (4, 2500, 8.0, 'Excellent', 9200, 45, 380, 'Hit water goal! Jogged in park'),
            (3, 2300, 7.0, 'Good', 8100, 40, 330, 'Good sleep and recovery'),
            (2, 2000, 6.8, 'Fair', 6700, 25, 275, 'Moderate routine'),
            (1, 2600, 8.2, 'Excellent', 10150, 50, 420, 'Long weekend walk'),
            (0, 1750, 7.2, 'Good', 6450, 30, 260, 'Today so far'),
        ]
        now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
        for days_ago, water, sleep, quality, steps, active, cal, notes in sample_data:
            rec_date = (today - datetime.timedelta(days=days_ago)).isoformat()
            cursor.execute("""
                INSERT OR IGNORE INTO wellness_records 
                (record_date, water_ml, sleep_hours, sleep_quality, steps, active_minutes, calories_burned, notes, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (rec_date, water, sleep, quality, steps, active, cal, notes, now_iso))
            
    conn.commit()
    conn.close()

