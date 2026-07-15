"""Kivy Screens for the Micah AI Tutor application"""

from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class WelcomeScreen(Screen):
    """Welcome screen with app introduction"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(
            text='🧬 Micah - Science AI Tutor',
            font_size='32sp',
            bold=True,
            size_hint_y=0.2
        )
        
        subtitle = Label(
            text='Your Personal AI Science Tutor',
            font_size='18sp',
            size_hint_y=0.1
        )
        
        description = Label(
            text=(
                'Learn science with personalized AI tutoring.\n\n'
                'Features:\n'
                '✨ Adaptive learning paths\n'
                '🤖 AI-powered Q&A\n'
                '📊 Progress tracking\n'
                '🎯 Personalized recommendations'
            ),
            font_size='14sp',
            size_hint_y=0.4
        )
        
        btn_layout = BoxLayout(size_hint_y=0.3, spacing=10)
        
        login_btn = Button(
            text='Login',
            size_hint_x=0.5,
            background_color=(0.2, 0.6, 1, 1)
        )
        login_btn.bind(on_press=self.go_to_login)
        
        signup_btn = Button(
            text='Sign Up',
            size_hint_x=0.5,
            background_color=(0.2, 0.8, 0.2, 1)
        )
        signup_btn.bind(on_press=self.go_to_signup)
        
        btn_layout.add_widget(login_btn)
        btn_layout.add_widget(signup_btn)
        
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(description)
        layout.add_widget(btn_layout)
        
        self.add_widget(layout)
    
    def go_to_login(self, instance):
        self.manager.current = 'login'
    
    def go_to_signup(self, instance):
        self.manager.current = 'login'

class LoginScreen(Screen):
    """Login/Sign up screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text='Welcome Back!',
            font_size='28sp',
            bold=True,
            size_hint_y=0.15
        )
        
        # Email field
        email_label = Label(text='Email:', size_hint_y=0.08, font_size='14sp')
        self.email_input = TextInput(
            multiline=False,
            size_hint_y=0.1,
            hint_text='Enter your email'
        )
        
        # Password field
        pass_label = Label(text='Password:', size_hint_y=0.08, font_size='14sp')
        self.pass_input = TextInput(
            multiline=False,
            password=True,
            size_hint_y=0.1,
            hint_text='Enter your password'
        )
        
        # Buttons
        btn_layout = BoxLayout(size_hint_y=0.15, spacing=10)
        
        login_btn = Button(
            text='Login',
            background_color=(0.2, 0.6, 1, 1)
        )
        login_btn.bind(on_press=self.authenticate)
        
        back_btn = Button(
            text='Back',
            background_color=(0.8, 0.8, 0.8, 1)
        )
        back_btn.bind(on_press=self.go_back)
        
        btn_layout.add_widget(back_btn)
        btn_layout.add_widget(login_btn)
        
        layout.add_widget(title)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(pass_label)
        layout.add_widget(self.pass_input)
        layout.add_widget(btn_layout)
        
        self.add_widget(layout)
    
    def authenticate(self, instance):
        self.manager.current = 'dashboard'
    
    def go_back(self, instance):
        self.manager.current = 'welcome'

class DashboardScreen(Screen):
    """Main dashboard with learning options"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        header = Label(
            text='📊 Your Dashboard',
            font_size='24sp',
            bold=True,
            size_hint_y=0.1
        )
        
        # Stats
        stats_layout = GridLayout(
            cols=3,
            spacing=10,
            size_hint_y=0.15,
            padding=10
        )
        
        stats_layout.add_widget(Label(text='📚 Lessons\n5', font_size='12sp'))
        stats_layout.add_widget(Label(text='⭐ XP Points\n250', font_size='12sp'))
        stats_layout.add_widget(Label(text='🔥 Streak\n7 days', font_size='12sp'))
        
        # Subject buttons
        subjects_title = Label(
            text='Choose a Subject:',
            font_size='16sp',
            bold=True,
            size_hint_y=0.08
        )
        
        subjects = ['🧬 Biology', '⚗️ Chemistry', '⚛️ Physics', '🌍 Earth Science']
        subjects_layout = GridLayout(
            cols=2,
            spacing=10,
            size_hint_y=0.35,
            padding=10
        )
        
        for subject in subjects:
            btn = Button(
                text=subject,
                background_color=(0.2, 0.6, 1, 1),
                size_hint_y=0.5
            )
            btn.bind(on_press=self.select_subject)
            subjects_layout.add_widget(btn)
        
        # Bottom buttons
        bottom_layout = BoxLayout(size_hint_y=0.12, spacing=10)
        
        qa_btn = Button(
            text='❓ Ask AI Questions',
            background_color=(0.8, 0.2, 0.8, 1)
        )
        qa_btn.bind(on_press=self.go_to_qa)
        
        profile_btn = Button(
            text='👤 Profile',
            background_color=(0.2, 0.8, 0.2, 1)
        )
        profile_btn.bind(on_press=self.go_to_profile)
        
        bottom_layout.add_widget(qa_btn)
        bottom_layout.add_widget(profile_btn)
        
        layout.add_widget(header)
        layout.add_widget(stats_layout)
        layout.add_widget(subjects_title)
        layout.add_widget(subjects_layout)
        layout.add_widget(bottom_layout)
        
        self.add_widget(layout)
    
    def select_subject(self, instance):
        self.manager.current = 'lesson'
    
    def go_to_qa(self, instance):
        self.manager.current = 'qa'
    
    def go_to_profile(self, instance):
        pass

class LessonScreen(Screen):
    """Interactive lesson screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = Label(
            text='🧬 Photosynthesis - Biology',
            font_size='22sp',
            bold=True,
            size_hint_y=0.1
        )
        
        # Content area
        scroll = ScrollView(size_hint_y=0.6)
        content_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        lesson_text = Label(
            text=(
                'Photosynthesis is the process by which plants convert light energy into chemical energy...\n\n'
                'Key Points:\n'
                '• Occurs in chloroplasts\n'
                '• Requires sunlight, water, and CO2\n'
                '• Produces glucose and oxygen\n\n'
                'Formula: 6CO2 + 6H2O + light → C6H12O6 + 6O2'
            ),
            font_size='13sp',
            size_hint_y=None,
            height=300
        )
        
        content_layout.add_widget(lesson_text)
        scroll.add_widget(content_layout)
        
        # Quiz buttons
        quiz_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        
        quiz_btn = Button(
            text='📝 Take Quiz',
            background_color=(0.2, 0.6, 1, 1)
        )
        
        back_btn = Button(
            text='← Back',
            background_color=(0.8, 0.8, 0.8, 1)
        )
        back_btn.bind(on_press=self.go_back)
        
        quiz_layout.add_widget(back_btn)
        quiz_layout.add_widget(quiz_btn)
        
        layout.add_widget(header)
        layout.add_widget(scroll)
        layout.add_widget(quiz_layout)
        
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'dashboard'

class QAScreen(Screen):
    """AI Question & Answer screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = Label(
            text='🤖 Ask Micah AI',
            font_size='24sp',
            bold=True,
            size_hint_y=0.1
        )
        
        # Chat area
        self.chat_label = Label(
            text='Hello! I\'m Micah, your AI Science Tutor. Ask me anything about science!',
            font_size='13sp',
            size_hint_y=0.5
        )
        
        # Question input
        self.question_input = TextInput(
            multiline=True,
            size_hint_y=0.2,
            hint_text='Ask your science question here...'
        )
        
        # Button layout
        btn_layout = BoxLayout(size_hint_y=0.15, spacing=10)
        
        ask_btn = Button(
            text='Ask',
            background_color=(0.2, 0.6, 1, 1)
        )
        ask_btn.bind(on_press=self.ask_question)
        
        back_btn = Button(
            text='Back',
            background_color=(0.8, 0.8, 0.8, 1)
        )
        back_btn.bind(on_press=self.go_back)
        
        btn_layout.add_widget(back_btn)
        btn_layout.add_widget(ask_btn)
        
        layout.add_widget(header)
        layout.add_widget(self.chat_label)
        layout.add_widget(self.question_input)
        layout.add_widget(btn_layout)
        
        self.add_widget(layout)
    
    def ask_question(self, instance):
        question = self.question_input.text
        if question:
            self.chat_label.text = f'Q: {question}\n\nA: Processing your question...'
            self.question_input.text = ''
    
    def go_back(self, instance):
        self.manager.current = 'dashboard'
