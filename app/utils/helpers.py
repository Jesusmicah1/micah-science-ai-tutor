"""Helper Functions - Utility functions for the application"""

import uuid
import hashlib
from typing import Any, Dict, List

def generate_id() -> str:
    """Generate a unique ID"""
    return str(uuid.uuid4())

def hash_password(password: str) -> str:
    """Hash a password"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hash_value: str) -> bool:
    """Verify a password against its hash"""
    return hashlib.sha256(password.encode()).hexdigest() == hash_value

def validate_email(email: str) -> bool:
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_duration(seconds: int) -> str:
    """Format duration in human-readable format"""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes}m"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m"

def calculate_accuracy(correct: int, total: int) -> float:
    """Calculate accuracy percentage"""
    return (correct / total * 100) if total > 0 else 0.0

def calculate_xp_earned(difficulty: str, is_correct: bool) -> int:
    """Calculate XP earned for a question"""
    base_xp = {
        'Beginner': 10,
        'Intermediate': 20,
        'Advanced': 30,
        'Expert': 50,
    }
    
    xp = base_xp.get(difficulty, 10)
    return xp if is_correct else xp // 2

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
