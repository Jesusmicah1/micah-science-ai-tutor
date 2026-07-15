"""Recommendation Engine - Personalized learning recommendations"""

from typing import List, Dict
from datetime import datetime, timedelta

class RecommendationEngine:
    """Generate personalized learning recommendations"""
    
    def __init__(self):
        """Initialize recommendation engine"""
        self.user_interactions = {}
        self.content_ratings = {}
    
    def recommend_topics(self, student_id: str, subject: str, history: Dict) -> List[str]:
        """Recommend topics based on learning history"""
        # Analyze what the student has learned
        learned_topics = history.get('learned_topics', [])
        
        # Get all available topics for subject
        all_topics = self._get_subject_topics(subject)
        
        # Filter out already learned topics
        remaining_topics = [t for t in all_topics if t not in learned_topics]
        
        # Score topics based on dependencies and difficulty
        scored_topics = self._score_topics(remaining_topics, history)
        
        # Return top recommendations
        return sorted(scored_topics, key=lambda x: x['score'], reverse=True)[:5]
    
    def recommend_difficulty_level(self, student_id: str, performance_history: List[float]) -> str:
        """Recommend appropriate difficulty level"""
        if not performance_history:
            return 'Beginner'
        
        avg_performance = sum(performance_history[-10:]) / min(10, len(performance_history))
        
        if avg_performance >= 0.9:
            return 'Expert'
        elif avg_performance >= 0.75:
            return 'Advanced'
        elif avg_performance >= 0.6:
            return 'Intermediate'
        else:
            return 'Beginner'
    
    def recommend_next_lesson(self, student_id: str, current_subject: str, history: Dict) -> Dict:
        """Recommend the next lesson to take"""
        topics = self.recommend_topics(student_id, current_subject, history)
        
        if topics:
            next_topic = topics[0]['name']
            difficulty = self.recommend_difficulty_level(student_id, history.get('performance', []))
            
            return {
                'topic': next_topic,
                'difficulty': difficulty,
                'estimated_duration': '15 minutes',
                'reason': f"Based on your learning progress, this topic will help strengthen your understanding.",
            }
        
        return {}
    
    def recommend_review_content(self, student_id: str, history: Dict) -> List[Dict]:
        """Recommend content to review using spaced repetition"""
        review_content = []
        learned_topics = history.get('learned_topics', [])
        last_review_dates = history.get('last_review_dates', {})
        
        for topic in learned_topics:
            last_review = last_review_dates.get(topic, datetime.now() - timedelta(days=7))
            days_since_review = (datetime.now() - last_review).days
            
            # Spaced repetition intervals: 1 day, 3 days, 7 days, 14 days, 30 days
            if days_since_review >= 1:  # Recommend for review
                review_content.append({
                    'topic': topic,
                    'last_reviewed': last_review,
                    'days_since_review': days_since_review,
                    'priority': min(days_since_review / 30, 1.0),  # Higher priority for older reviews
                })
        
        return sorted(review_content, key=lambda x: x['priority'], reverse=True)[:5]
    
    def get_learning_insights(self, student_id: str, history: Dict) -> Dict:
        """Generate insights about student learning"""
        accuracy = history.get('accuracy_rate', 0)
        topics_learned = len(history.get('learned_topics', []))
        xp_points = history.get('xp_points', 0)
        
        insights = {
            'strong_areas': self._identify_strong_areas(history),
            'needs_improvement': self._identify_weak_areas(history),
            'recommended_actions': self._generate_recommendations(accuracy, topics_learned),
            'learning_velocity': self._calculate_learning_velocity(history),
            'next_milestone': self._calculate_next_milestone(xp_points),
        }
        
        return insights
    
    def _get_subject_topics(self, subject: str) -> List[str]:
        """Get all topics for a subject"""
        topics = {
            'Biology': [
                'Cell Structure',
                'Photosynthesis',
                'Respiration',
                'Genetics',
                'Evolution',
                'Ecosystems',
                'Human Body',
                'Reproduction',
            ],
            'Chemistry': [
                'Atoms & Electrons',
                'Periodic Table',
                'Bonding',
                'Reactions',
                'Stoichiometry',
                'Acids & Bases',
                'Oxidation & Reduction',
                'States of Matter',
            ],
            'Physics': [
                'Motion & Forces',
                'Energy',
                'Waves',
                'Electricity',
                'Magnetism',
                'Light',
                'Modern Physics',
                'Thermodynamics',
            ],
            'Earth Science': [
                'Plate Tectonics',
                'Rock Cycle',
                'Weather & Climate',
                'Atmosphere',
                'Water Cycle',
                'Astronomy',
                'Geology',
                'Environmental Science',
            ],
        }
        return topics.get(subject, [])
    
    def _score_topics(self, topics: List[str], history: Dict) -> List[Dict]:
        """Score topics based on dependencies and difficulty"""
        scored = []
        for topic in topics:
            score = 0.5  # Base score
            # Adjust based on prerequisites, student level, etc.
            scored.append({'name': topic, 'score': score})
        return scored
    
    def _identify_strong_areas(self, history: Dict) -> List[str]:
        """Identify topics where student excels"""
        return history.get('strong_areas', [])
    
    def _identify_weak_areas(self, history: Dict) -> List[str]:
        """Identify topics that need improvement"""
        return history.get('weak_areas', [])
    
    def _generate_recommendations(self, accuracy: float, topics_learned: int) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        if accuracy < 0.6:
            recommendations.append('Consider reviewing previous lessons')
        if topics_learned < 5:
            recommendations.append('Keep progressing through the curriculum')
        
        return recommendations
    
    def _calculate_learning_velocity(self, history: Dict) -> str:
        """Calculate how fast the student is learning"""
        return 'Steady Progress'
    
    def _calculate_next_milestone(self, xp_points: int) -> Dict:
        """Calculate next achievement milestone"""
        milestones = [100, 250, 500, 1000, 2500, 5000]
        next_milestone = next((m for m in milestones if m > xp_points), 5000)
        
        return {
            'milestone': next_milestone,
            'current': xp_points,
            'remaining': next_milestone - xp_points,
        }
