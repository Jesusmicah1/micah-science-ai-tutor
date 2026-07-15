"""Science Curriculum Modules - Educational content organized by subject"""

from typing import Dict, List

class ScienceModule:
    """Base science module for curriculum"""
    
    def __init__(self, name: str, subject: str, level: str):
        self.name = name
        self.subject = subject
        self.level = level
        self.lessons = []
        self.quizzes = []
    
    def add_lesson(self, lesson: Dict):
        """Add a lesson to the module"""
        self.lessons.append(lesson)
    
    def get_lessons(self) -> List[Dict]:
        """Get all lessons in the module"""
        return self.lessons

class BiologyModule(ScienceModule):
    """Biology curriculum module"""
    
    def __init__(self):
        super().__init__('Biology', 'Biology', 'All Levels')
        self._initialize_lessons()
    
    def _initialize_lessons(self):
        """Initialize biology lessons"""
        lessons = [
            {
                'id': 'bio_001',
                'title': 'Cell Structure and Function',
                'description': 'Learn about the basic building blocks of life',
                'content': (
                    'Cells are the fundamental units of life. All living organisms are composed of one or more cells. '
                    'There are two main types: prokaryotic and eukaryotic cells.'
                ),
                'duration': '15 minutes',
                'difficulty': 'Beginner',
                'keywords': ['cell', 'organelles', 'membrane', 'nucleus'],
            },
            {
                'id': 'bio_002',
                'title': 'Photosynthesis',
                'description': 'Understand how plants convert light energy to chemical energy',
                'content': (
                    'Photosynthesis is the process by which plants, algae, and some bacteria convert light energy '
                    'into chemical energy. The overall equation is: 6CO2 + 6H2O + light energy → C6H12O6 + 6O2'
                ),
                'duration': '20 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['photosynthesis', 'chlorophyll', 'glucose', 'oxygen'],
            },
            {
                'id': 'bio_003',
                'title': 'Genetics and Inheritance',
                'description': 'Explore how traits are passed from parents to offspring',
                'content': (
                    'Genetics is the study of heredity and genes. Mendel\'s laws of inheritance explain how traits '
                    'are passed from parent organisms to their offspring.'
                ),
                'duration': '25 minutes',
                'difficulty': 'Advanced',
                'keywords': ['dna', 'genes', 'inheritance', 'alleles'],
            },
        ]
        
        for lesson in lessons:
            self.add_lesson(lesson)

class ChemistryModule(ScienceModule):
    """Chemistry curriculum module"""
    
    def __init__(self):
        super().__init__('Chemistry', 'Chemistry', 'All Levels')
        self._initialize_lessons()
    
    def _initialize_lessons(self):
        """Initialize chemistry lessons"""
        lessons = [
            {
                'id': 'chem_001',
                'title': 'Atoms and Electrons',
                'description': 'Understand the structure of atoms and electron configuration',
                'content': (
                    'Atoms are the basic units of matter. They consist of a nucleus (protons and neutrons) '
                    'surrounded by electrons in electron shells.'
                ),
                'duration': '18 minutes',
                'difficulty': 'Beginner',
                'keywords': ['atom', 'electron', 'proton', 'nucleus'],
            },
            {
                'id': 'chem_002',
                'title': 'Chemical Bonding',
                'description': 'Learn about ionic and covalent bonds',
                'content': (
                    'Chemical bonds form between atoms to create molecules. The main types are ionic bonds '
                    '(transfer of electrons) and covalent bonds (sharing of electrons).'
                ),
                'duration': '22 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['bonding', 'ionic', 'covalent', 'molecule'],
            },
            {
                'id': 'chem_003',
                'title': 'Oxidation and Reduction',
                'description': 'Understand redox reactions',
                'content': (
                    'Oxidation-reduction (redox) reactions involve the transfer of electrons between substances. '
                    'Oxidation is loss of electrons, and reduction is gain of electrons.'
                ),
                'duration': '25 minutes',
                'difficulty': 'Advanced',
                'keywords': ['oxidation', 'reduction', 'electron', 'transfer'],
            },
        ]
        
        for lesson in lessons:
            self.add_lesson(lesson)

class PhysicsModule(ScienceModule):
    """Physics curriculum module"""
    
    def __init__(self):
        super().__init__('Physics', 'Physics', 'All Levels')
        self._initialize_lessons()
    
    def _initialize_lessons(self):
        """Initialize physics lessons"""
        lessons = [
            {
                'id': 'phys_001',
                'title': 'Motion and Forces',
                'description': 'Learn Newton\'s laws of motion',
                'content': (
                    'Newton\'s three laws of motion describe how objects move and respond to forces. '
                    '1st Law: An object at rest stays at rest. 2nd Law: F=ma. 3rd Law: Action = Reaction.'
                ),
                'duration': '20 minutes',
                'difficulty': 'Beginner',
                'keywords': ['motion', 'force', 'Newton', 'acceleration'],
            },
            {
                'id': 'phys_002',
                'title': 'Energy and Work',
                'description': 'Understand kinetic and potential energy',
                'content': (
                    'Energy is the capacity to do work. Kinetic energy is energy of motion. '
                    'Potential energy is stored energy based on position or configuration.'
                ),
                'duration': '18 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['energy', 'work', 'kinetic', 'potential'],
            },
            {
                'id': 'phys_003',
                'title': 'Waves and Light',
                'description': 'Explore wave properties and electromagnetic radiation',
                'content': (
                    'Waves are disturbances that transfer energy. Light is an electromagnetic wave '
                    'that travels at 3×10^8 m/s. Wavelength and frequency are inversely related.'
                ),
                'duration': '25 minutes',
                'difficulty': 'Advanced',
                'keywords': ['wave', 'light', 'frequency', 'wavelength'],
            },
        ]
        
        for lesson in lessons:
            self.add_lesson(lesson)

class EarthScienceModule(ScienceModule):
    """Earth Science curriculum module"""
    
    def __init__(self):
        super().__init__('Earth Science', 'Earth Science', 'All Levels')
        self._initialize_lessons()
    
    def _initialize_lessons(self):
        """Initialize earth science lessons"""
        lessons = [
            {
                'id': 'earth_001',
                'title': 'Plate Tectonics',
                'description': 'Understand the movement of Earth\'s crust',
                'content': (
                    'Earth\'s crust is divided into several plates that move slowly. This movement causes '
                    'earthquakes, volcanoes, and mountain formation at plate boundaries.'
                ),
                'duration': '22 minutes',
                'difficulty': 'Beginner',
                'keywords': ['plate', 'tectonics', 'earthquake', 'volcano'],
            },
            {
                'id': 'earth_002',
                'title': 'Weather and Climate',
                'description': 'Learn about atmospheric processes and climate patterns',
                'content': (
                    'Weather is short-term atmospheric conditions, while climate is long-term. '
                    'The sun\'s energy drives weather and climate systems on Earth.'
                ),
                'duration': '20 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['weather', 'climate', 'atmosphere', 'precipitation'],
            },
            {
                'id': 'earth_003',
                'title': 'Water Cycle',
                'description': 'Understand the continuous movement of water on Earth',
                'content': (
                    'The water cycle (hydrologic cycle) involves evaporation, condensation, precipitation, and '
                    'collection. Water continuously moves between atmosphere, land, and oceans.'
                ),
                'duration': '18 minutes',
                'difficulty': 'Advanced',
                'keywords': ['water cycle', 'evaporation', 'condensation', 'precipitation'],
            },
        ]
        
        for lesson in lessons:
            self.add_lesson(lesson)

class CurriculumManager:
    """Manage all science curriculum modules"""
    
    def __init__(self):
        """Initialize curriculum manager"""
        self.modules = {
            'Biology': BiologyModule(),
            'Chemistry': ChemistryModule(),
            'Physics': PhysicsModule(),
            'Earth Science': EarthScienceModule(),
        }
    
    def get_module(self, subject: str) -> ScienceModule:
        """Get a specific module"""
        return self.modules.get(subject)
    
    def get_all_modules(self) -> Dict[str, ScienceModule]:
        """Get all modules"""
        return self.modules
    
    def search_lessons(self, query: str) -> List[Dict]:
        """Search for lessons by keyword"""
        results = []
        
        for module in self.modules.values():
            for lesson in module.get_lessons():
                if (query.lower() in lesson['title'].lower() or
                    query.lower() in lesson['description'].lower() or
                    any(query.lower() in keyword for keyword in lesson.get('keywords', []))):
                    results.append(lesson)
        
        return results
