# Micah - Science AI Tutor

🚀 An intelligent mobile app for personalized science education powered by AI.

## Features

✨ **AI-Powered Learning**
- Personalized tutoring based on student progress
- Natural language question answering
- Adaptive difficulty levels

📊 **Progress Tracking**
- Real-time performance analytics
- Learning insights and recommendations
- Goal tracking

🧬 **Science Curriculum**
- Biology, Chemistry, Physics, Earth Science
- Interactive lessons and explanations
- Hands-on experiments and demonstrations

🎯 **Smart Features**
- Personalized content recommendations
- Spaced repetition for better retention
- Multi-topic learning paths

## Tech Stack

- **Frontend**: Kivy (Python cross-platform mobile)
- **Backend**: Python with Flask
- **AI/ML**: scikit-learn, NLTK, TensorFlow
- **Database**: SQLite (local) / Firebase (cloud)
- **API Integration**: OpenAI GPT, Google Custom Search

## Installation

### Prerequisites
- Python 3.8+
- pip package manager
- Kivy framework

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Jesusmicah1/micah-science-ai-tutor.git
cd micah-science-ai-tutor
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python main.py
```

## Project Structure

```
micah-science-ai-tutor/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── config.py              # Configuration settings
├── README.md              # This file
│
├── app/
│   ├── __init__.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── screens.py     # Kivy screens
│   │   └── styles.kv      # Kivy styling
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── tutor.py       # AI tutoring engine
│   │   ├── nlp.py         # Natural language processing
│   │   └── recommendations.py # Personalization engine
│   │
│   ├── content/
│   │   ├── __init__.py
│   │   ├── science_modules.py # Science curriculum
│   │   └── lessons.json   # Lesson data
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py         # Database operations
│   │   └── models.py     # Data models
│   │
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py    # Utility functions
│       └── analytics.py  # Progress tracking
│
└── tests/
    ├── __init__.py
    ├── test_ai.py
    └── test_content.py
```

## Usage

1. **Start Learning**: Launch the app and create an account
2. **Choose Subject**: Select from Biology, Chemistry, Physics, or Earth Science
3. **Get Personalized Content**: AI analyzes your learning style
4. **Ask Questions**: Natural language Q&A system answers your questions
5. **Track Progress**: View analytics and personalized recommendations
6. **Continue Learning**: Follow adaptive learning paths

## Configuration

Edit `config.py` to customize:
- AI model selection
- Database settings
- API keys (OpenAI, Google)
- Learning parameters

## API Keys

Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_key_here
GOOGLE_SEARCH_API_KEY=your_key_here
GOOGLE_SEARCH_ENGINE_ID=your_id_here
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For issues or questions, please create an issue on GitHub.

---

**Built with ❤️ by Jesusmicah1**
