"""Tests for science content modules"""

import unittest
from app.content.science_modules import CurriculumManager

class TestCurriculumManager(unittest.TestCase):
    """Test science curriculum"""
    
    def setUp(self):
        self.curriculum = CurriculumManager()
    
    def test_get_module(self):
        """Test getting a specific module"""
        biology = self.curriculum.get_module('Biology')
        self.assertIsNotNone(biology)
        self.assertEqual(biology.name, 'Biology')
    
    def test_get_lessons(self):
        """Test getting lessons from a module"""
        biology = self.curriculum.get_module('Biology')
        lessons = biology.get_lessons()
        
        self.assertIsInstance(lessons, list)
        self.assertTrue(len(lessons) > 0)
    
    def test_search_lessons(self):
        """Test searching for lessons"""
        results = self.curriculum.search_lessons('photosynthesis')
        
        self.assertIsInstance(results, list)
        self.assertTrue(len(results) > 0)

if __name__ == '__main__':
    unittest.main()
