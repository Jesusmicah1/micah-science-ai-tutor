"""Analytics Module - Learning analytics and progress tracking"""

from typing import Dict, List
from datetime import datetime, timedelta

class LearningAnalytics:
    """Track and analyze learning progress"""
    
    def __init__(self):
        """Initialize analytics"""
        self.user_data = {}
    
    def track_session(self, user_id: str, subject: str, duration: int, questions_answered: int, accuracy: float):
        """Track a learning session"""
        if user_id not in self.user_data:
            self.user_data[user_id] = []
        
        session = {
            'timestamp': datetime.now(),
            'subject': subject,
            'duration': duration,
            'questions': questions_answered,
            'accuracy': accuracy,
        }
        
        self.user_data[user_id].append(session)
    
    def get_daily_stats(self, user_id: str, days: int = 7) -> Dict:
        """Get daily statistics"""
        if user_id not in self.user_data:
            return {}
        
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_sessions = [
            s for s in self.user_data[user_id]
            if s['timestamp'] > cutoff_date
        ]
        
        return {
            'total_sessions': len(recent_sessions),
            'total_time': sum(s['duration'] for s in recent_sessions),
            'total_questions': sum(s['questions'] for s in recent_sessions),
            'average_accuracy': (
                sum(s['accuracy'] for s in recent_sessions) / len(recent_sessions)
                if recent_sessions else 0
            ),
        }
    
    def get_subject_progress(self, user_id: str) -> Dict[str, float]:
        """Get progress by subject"""
        if user_id not in self.user_data:
            return {}
        
        subjects = {}
        for session in self.user_data[user_id]:
            subject = session['subject']
            if subject not in subjects:
                subjects[subject] = []
            subjects[subject].append(session['accuracy'])
        
        return {
            subject: sum(scores) / len(scores)
            for subject, scores in subjects.items()
        }
    
    def calculate_learning_velocity(self, user_id: str) -> float:
        """Calculate how fast the user is learning (XP per day)"""
        if user_id not in self.user_data or not self.user_data[user_id]:
            return 0.0
        
        sessions = self.user_data[user_id]
        days_active = (
            sessions[-1]['timestamp'] - sessions[0]['timestamp']
        ).days + 1
        
        total_xp = sum(
            (s['questions'] * s['accuracy']) for s in sessions
        )
        
        return total_xp / days_active if days_active > 0 else 0.0
    
    def generate_report(self, user_id: str) -> Dict:
        """Generate comprehensive learning report"""
        return {
            'user_id': user_id,
            'daily_stats': self.get_daily_stats(user_id),
            'subject_progress': self.get_subject_progress(user_id),
            'learning_velocity': self.calculate_learning_velocity(user_id),
            'generated_at': datetime.now().isoformat(),
        }
