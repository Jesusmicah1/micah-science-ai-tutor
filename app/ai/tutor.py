"""AI Tutoring Engine - Core AI logic for personalized learning"""

import json
from typing import Dict, List, Optional
from config import AI_CONFIG

class AITutor:
    """Main AI tutor class handling personalized learning"""
    
    def __init__(self):
        """Initialize the AI tutor"""
        self.model = AI_CONFIG['model']
        self.api_key = AI_CONFIG['api_key']
        self.temperature = AI_CONFIG['temperature']
        self.max_tokens = AI_CONFIG['max_tokens']
        self.student_profiles = {}
        self.learning_history = {}
    
    def create_student_profile(self, student_id: str, name: str, age: int, subjects: List[str]) -> Dict:
        """Create a new student profile"""
        profile = {
            'student_id': student_id,
            'name': name,
            'age': age,
            'subjects': subjects,
            'difficulty_level': 'Beginner',
            'xp_points': 0,
            'streak_days': 0,
            'total_questions_answered': 0,
            'accuracy_rate': 0.0,
            'learning_style': self._analyze_learning_style(student_id),
            'recommended_topics': [],
        }
        self.student_profiles[student_id] = profile
        return profile
    
    def personalize_content(self, student_id: str, subject: str) -> Dict:
        """Generate personalized content recommendations"""
        profile = self.student_profiles.get(student_id)
        if not profile:
            return {}
        
        recommendations = {
            'student_id': student_id,
            'subject': subject,
            'difficulty': profile['difficulty_level'],
            'topics': self._generate_topic_recommendations(student_id, subject),
            'learning_path': self._generate_learning_path(student_id, subject),
            'focus_areas': self._identify_focus_areas(student_id, subject),
        }
        
        return recommendations
    
    def answer_question(self, question: str, subject: str, difficulty: str) -> str:
        """Generate AI-powered answer to student questions"""
        # This would integrate with OpenAI API in production
        context = {
            'question': question,
            'subject': subject,
            'difficulty': difficulty,
        }
        
        answer = self._generate_answer(context)
        return answer
    
    def evaluate_response(self, student_id: str, question: str, answer: str, correct_answer: str) -> Dict:
        """Evaluate student response and provide feedback"""
        evaluation = {
            'student_id': student_id,
            'is_correct': answer.lower() == correct_answer.lower(),
            'feedback': self._generate_feedback(answer, correct_answer),
            'xp_earned': 10 if answer.lower() == correct_answer.lower() else 5,
            'explanation': self._generate_explanation(answer, correct_answer),
        }
        
        return evaluation
    
    def update_difficulty(self, student_id: str, performance: float) -> str:
        """Adjust difficulty based on student performance"""
        profile = self.student_profiles.get(student_id)
        if not profile:
            return profile['difficulty_level']
        
        current_difficulty = profile['difficulty_level']
        
        if performance >= 0.9:
            new_difficulty = 'Advanced'
        elif performance >= 0.75:
            new_difficulty = 'Intermediate'
        elif performance >= 0.5:
            new_difficulty = 'Beginner'
        else:
            new_difficulty = 'Beginner'
        
        profile['difficulty_level'] = new_difficulty
        return new_difficulty
    
    def _analyze_learning_style(self, student_id: str) -> str:
        """Analyze student learning style"""
        # Visual, Auditory, Reading/Writing, Kinesthetic
        return 'Visual'
    
    def _generate_topic_recommendations(self, student_id: str, subject: str) -> List[str]:
        """Generate recommended topics for the student"""
        topics = {
            'Biology': ['Cell Structure', 'Genetics', 'Evolution', 'Photosynthesis', 'Ecosystems'],
            'Chemistry': ['Atoms', 'Molecules', 'Chemical Reactions', 'Periodic Table', 'Bonding'],
            'Physics': ['Motion', 'Forces', 'Energy', 'Waves', 'Electricity'],
            'Earth Science': ['Plate Tectonics', 'Weather', 'Atmosphere', 'Water Cycle', 'Rocks'],
        }
        return topics.get(subject, [])
    
    def _generate_learning_path(self, student_id: str, subject: str) -> List[str]:
        """Generate a personalized learning path"""
        return [
            'Introduction to Topic',
            'Core Concepts',
            'Examples & Applications',
            'Practice Problems',
            'Quiz & Assessment',
        ]
    
    def _identify_focus_areas(self, student_id: str, subject: str) -> List[str]:
        """Identify areas the student needs to focus on"""
        return ['Concept Understanding', 'Problem Solving', 'Application']
    
    def _generate_answer(self, context: Dict) -> str:
        """Generate an answer using AI"""
        # Integration with OpenAI API would happen here
        return "This is an AI-generated answer based on your question and difficulty level."
    
    def _generate_feedback(self, answer: str, correct_answer: str) -> str:
        """Generate feedback for student response"""
        if answer.lower() == correct_answer.lower():
            return "Excellent! Your answer is correct! 🎉"
        else:
            return "Not quite right. Let me help you understand this better."
    
    def _generate_explanation(self, answer: str, correct_answer: str) -> str:
        """Generate detailed explanation"""
        return "Here's a detailed explanation of why the correct answer is the best..."
