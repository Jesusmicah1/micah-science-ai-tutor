"""Natural Language Processing Module - For understanding student questions"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List, Dict

class NLPProcessor:
    """Natural Language Processing for student questions"""
    
    def __init__(self):
        """Initialize NLP processor"""
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet')
        
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
    
    def preprocess_question(self, question: str) -> List[str]:
        """Preprocess student question"""
        # Tokenize
        tokens = word_tokenize(question.lower())
        
        # Remove stopwords and lemmatize
        processed = [
            self.lemmatizer.lemmatize(token)
            for token in tokens
            if token.isalnum() and token not in self.stop_words
        ]
        
        return processed
    
    def extract_keywords(self, question: str) -> List[str]:
        """Extract keywords from question"""
        processed = self.preprocess_question(question)
        return processed
    
    def classify_question_type(self, question: str) -> str:
        """Classify the type of question"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ['what', 'which', 'define', 'mean']):
            return 'definition'
        elif any(word in question_lower for word in ['why', 'how', 'explain', 'describe']):
            return 'explanation'
        elif any(word in question_lower for word in ['compare', 'difference', 'similar']):
            return 'comparison'
        elif any(word in question_lower for word in ['calculate', 'solve', 'compute', 'find']):
            return 'calculation'
        else:
            return 'general'
    
    def identify_subject_area(self, question: str, available_subjects: List[str]) -> str:
        """Identify the subject area of the question"""
        keywords = self.extract_keywords(question)
        
        subject_keywords = {
            'Biology': ['cell', 'organism', 'dna', 'photosynthesis', 'genetics', 'evolution', 'ecosystem'],
            'Chemistry': ['atom', 'molecule', 'reaction', 'element', 'compound', 'periodic', 'bonding'],
            'Physics': ['force', 'motion', 'energy', 'velocity', 'acceleration', 'wave', 'electricity'],
            'Earth Science': ['earthquake', 'volcano', 'weather', 'climate', 'plate', 'rock', 'fossil'],
        }
        
        for subject, keywords_list in subject_keywords.items():
            if any(keyword in keywords for keyword in keywords_list):
                return subject
        
        return available_subjects[0] if available_subjects else 'General'
    
    def similarity_score(self, question1: str, question2: str) -> float:
        """Calculate similarity between two questions"""
        keywords1 = set(self.extract_keywords(question1))
        keywords2 = set(self.extract_keywords(question2))
        
        if not keywords1 or not keywords2:
            return 0.0
        
        intersection = len(keywords1.intersection(keywords2))
        union = len(keywords1.union(keywords2))
        
        return intersection / union if union > 0 else 0.0
