"""Data Models - Pydantic models for data validation"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    """User model"""
    user_id: str
    name: str
    email: str
    age: int
    created_at: datetime = datetime.now()

class StudentProfile(BaseModel):
    """Student profile model"""
    profile_id: str
    user_id: str
    xp_points: int = 0
    streak_days: int = 0
    total_questions: int = 0
    accuracy_rate: float = 0.0
    preferred_difficulty: str = "Beginner"

class LearningRecord(BaseModel):
    """Learning history record"""
    history_id: str
    user_id: str
    subject: str
    topic: str
    score: float
    time_spent: int
    completed_at: datetime = datetime.now()

class QuizResult(BaseModel):
    """Quiz result model"""
    result_id: str
    user_id: str
    quiz_id: str
    score: float
    answers: List[str]
    completed_at: datetime = datetime.now()

class Question(BaseModel):
    """Question model"""
    question_id: str
    subject: str
    topic: str
    question_text: str
    answer_text: str
    difficulty: str
    created_at: datetime = datetime.now()
