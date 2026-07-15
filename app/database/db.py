"""Database Operations - SQLite database management"""

import sqlite3
import os
from typing import Dict, List, Optional
from datetime import datetime

class Database:
    """SQLite database management"""
    
    def __init__(self, db_path: str = 'data/micah_tutor.db'):
        """Initialize database"""
        self.db_path = db_path
        self.connection = None
        self.cursor = None
    
    def initialize(self):
        """Initialize database and create tables"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        
        self._create_tables()
        print(f"✅ Database initialized at {self.db_path}")
    
    def _create_tables(self):
        """Create database tables"""
        # Users table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                password_hash TEXT,
                age INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Student profiles table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS student_profiles (
                profile_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                xp_points INTEGER DEFAULT 0,
                streak_days INTEGER DEFAULT 0,
                total_questions INTEGER DEFAULT 0,
                accuracy_rate REAL DEFAULT 0.0,
                preferred_difficulty TEXT DEFAULT "Beginner",
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Learning history table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS learning_history (
                history_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                subject TEXT NOT NULL,
                topic TEXT NOT NULL,
                score REAL,
                time_spent INTEGER,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Quiz results table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS quiz_results (
                result_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                quiz_id TEXT NOT NULL,
                score REAL,
                answers TEXT,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Questions table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                question_id TEXT PRIMARY KEY,
                subject TEXT NOT NULL,
                topic TEXT NOT NULL,
                question_text TEXT NOT NULL,
                answer_text TEXT NOT NULL,
                difficulty TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.connection.commit()
    
    def add_user(self, user_id: str, name: str, email: str, password_hash: str, age: int):
        """Add a new user"""
        self.cursor.execute('''
            INSERT INTO users (user_id, name, email, password_hash, age)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, name, email, password_hash, age))
        self.connection.commit()
    
    def add_learning_record(self, user_id: str, subject: str, topic: str, score: float, time_spent: int):
        """Add a learning record"""
        import uuid
        history_id = str(uuid.uuid4())
        
        self.cursor.execute('''
            INSERT INTO learning_history (history_id, user_id, subject, topic, score, time_spent)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (history_id, user_id, subject, topic, score, time_spent))
        self.connection.commit()
    
    def get_user_profile(self, user_id: str) -> Optional[Dict]:
        """Get user profile"""
        self.cursor.execute('SELECT * FROM student_profiles WHERE user_id = ?', (user_id,))
        result = self.cursor.fetchone()
        return dict(result) if result else None
    
    def update_user_xp(self, user_id: str, xp_points: int):
        """Update user XP points"""
        self.cursor.execute('''
            UPDATE student_profiles SET xp_points = xp_points + ?
            WHERE user_id = ?
        ''', (xp_points, user_id))
        self.connection.commit()
    
    def get_learning_history(self, user_id: str) -> List[Dict]:
        """Get user learning history"""
        self.cursor.execute(
            'SELECT * FROM learning_history WHERE user_id = ? ORDER BY completed_at DESC',
            (user_id,)
        )
        return [dict(row) for row in self.cursor.fetchall()]
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("✅ Database connection closed")
