"""Tests for AI Tutor module"""

import unittest
from app.ai.tutor import AITutor
from app.ai.nlp import NLPProcessor
from app.ai.recommendations import RecommendationEngine

class TestAITutor(unittest.TestCase):
    """Test AI Tutor functionality"""
    
    def setUp(self):
        self.tutor = AITutor()
    
    def test_create_student_profile(self):
        """Test creating a student profile"""
        profile = self.tutor.create_student_profile(
            'student_001',
            'John Doe',
            15,
            ['Biology', 'Chemistry']
        )
        
        self.assertEqual(profile['name'], 'John Doe')
        self.assertEqual(profile['age'], 15)
        self.assertEqual(profile['xp_points'], 0)
    
    def test_personalize_content(self):
        """Test content personalization"""
        self.tutor.create_student_profile(
            'student_001',
            'Jane Doe',
            14,
            ['Biology']
        )
        
        recommendations = self.tutor.personalize_content('student_001', 'Biology')
        
        self.assertIn('student_id', recommendations)
        self.assertIn('topics', recommendations)
        self.assertIn('learning_path', recommendations)

class TestNLPProcessor(unittest.TestCase):
    """Test NLP Processing"""
    
    def setUp(self):
        self.nlp = NLPProcessor()
    
    def test_preprocess_question(self):
        """Test question preprocessing"""
        question = "What is photosynthesis?"
        processed = self.nlp.preprocess_question(question)
        
        self.assertIsInstance(processed, list)
        self.assertTrue(len(processed) > 0)
    
    def test_classify_question_type(self):
        """Test question type classification"""
        question = "What is photosynthesis?"
        question_type = self.nlp.classify_question_type(question)
        
        self.assertIn(question_type, ['definition', 'explanation', 'comparison', 'calculation', 'general'])

if __name__ == '__main__':
    unittest.main()
