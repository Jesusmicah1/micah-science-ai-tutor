import os
from dotenv import load_dotenv

load_dotenv()

# App Configuration
APP_NAME = "Micah - Science AI Tutor"
APP_VERSION = "1.0.0"
DEBUG = True

# Kivy Configuration
KIVY_CONFIG = {
    'graphics': {
        'width': 800,
        'height': 600,
        'resizable': True,
        'orientation': 'portrait',
    },
    'input': {
        'mouse': 'mouse,multitouch_on_demand',
    }
}

# Database Configuration
DATABASE = {
    'path': 'data/micah_tutor.db',
    'backup_path': 'data/backups/',
}

# AI Configuration
AI_CONFIG = {
    'model': 'gpt-3.5-turbo',
    'temperature': 0.7,
    'max_tokens': 500,
    'api_key': os.getenv('OPENAI_API_KEY'),
}

# NLP Configuration
NLP_CONFIG = {
    'language': 'english',
    'tokenizer': 'punkt',
    'lemmatizer': True,
}

# Science Curriculum
SCIENCE_SUBJECTS = [
    'Biology',
    'Chemistry',
    'Physics',
    'Earth Science',
    'Astronomy',
]

# Learning Parameters
LEARNING_CONFIG = {
    'difficulty_levels': ['Beginner', 'Intermediate', 'Advanced', 'Expert'],
    'max_streak': 100,
    'xp_per_question': 10,
    'xp_per_lesson': 50,
    'spaced_repetition_enabled': True,
}

# Analytics Configuration
ANALYTICS = {
    'track_learning_path': True,
    'track_time_spent': True,
    'track_accuracy': True,
    'export_enabled': True,
}

# API Keys
APIS = {
    'openai_key': os.getenv('OPENAI_API_KEY'),
    'google_search_key': os.getenv('GOOGLE_SEARCH_API_KEY'),
    'google_search_engine_id': os.getenv('GOOGLE_SEARCH_ENGINE_ID'),
}
