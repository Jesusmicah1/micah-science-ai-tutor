#!/usr/bin/env python
"""
Micah - Science AI Tutor
An intelligent mobile app for personalized science education
"""

import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

from config import APP_NAME, APP_VERSION, KIVY_CONFIG
from app.ui.screens import WelcomeScreen, LoginScreen, DashboardScreen, LessonScreen, QAScreen
from app.database.db import Database
from app.ai.tutor import AITutor

# Set window size
Window.size = (KIVY_CONFIG['graphics']['width'], KIVY_CONFIG['graphics']['height'])

class MicahApp(App):
    """Main application class for Micah Science AI Tutor"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = f"{APP_NAME} v{APP_VERSION}"
        self.db = Database()
        self.ai_tutor = AITutor()
        
    def build(self):
        """Build the application UI"""
        self.root = ScreenManager()
        
        # Add screens
        self.root.add_widget(WelcomeScreen(name='welcome'))
        self.root.add_widget(LoginScreen(name='login'))
        self.root.add_widget(DashboardScreen(name='dashboard'))
        self.root.add_widget(LessonScreen(name='lesson'))
        self.root.add_widget(QAScreen(name='qa'))
        
        return self.root
    
    def on_start(self):
        """Called when the app starts"""
        print(f"\n{'='*50}")
        print(f"🚀 Welcome to {self.title}")
        print(f"{'='*50}\n")
        self.db.initialize()
        
    def on_stop(self):
        """Called when the app closes"""
        print(f"\n✨ Thank you for using {APP_NAME}!\n")
        self.db.close()

if __name__ == '__main__':
    app = MicahApp()
    app.run()
