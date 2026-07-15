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

class AgricultureModule(ScienceModule):
    """Agricultural Science curriculum module"""
    
    def __init__(self):
        super().__init__('Agricultural Science', 'Agricultural Science', 'All Levels')
        self._initialize_lessons()
    
    def _initialize_lessons(self):
        """Initialize agricultural science lessons"""
        lessons = [
            {
                'id': 'agri_001',
                'title': 'Soil Composition and Properties',
                'description': 'Understand soil structure, composition, and importance for farming',
                'content': (
                    'Soil is a complex mixture of mineral particles, organic matter, water, and air. '
                    'It consists of three main components: sand, silt, and clay. Soil pH, fertility, '
                    'and texture are critical factors for successful crop production. Soil provides:\n'
                    '• Mineral nutrients (nitrogen, phosphorus, potassium)\n'
                    '• Water retention\n'
                    '• Root support\n'
                    '• Habitat for beneficial microorganisms\n\n'
                    'Soil types vary by region and affect crop selection and farming techniques.'
                ),
                'duration': '20 minutes',
                'difficulty': 'Beginner',
                'keywords': ['soil', 'composition', 'pH', 'fertility', 'texture'],
            },
            {
                'id': 'agri_002',
                'title': 'Plant Nutrition and Fertilizers',
                'description': 'Learn about plant nutrients and how to optimize crop nutrition',
                'content': (
                    'Plants require 16 essential nutrients for growth and development:\n\n'
                    'Macronutrients (needed in large amounts):\n'
                    '• Nitrogen (N) - leaf and stem growth\n'
                    '• Phosphorus (P) - root development and flowering\n'
                    '• Potassium (K) - overall plant health\n'
                    '• Calcium (Ca), Magnesium (Mg), Sulfur (S)\n\n'
                    'Micronutrients (needed in small amounts):\n'
                    '• Iron, Zinc, Copper, Boron, Molybdenum, Manganese\n\n'
                    'Fertilizers can be organic (manure, compost) or synthetic (NPK compounds). '
                    'Proper nutrient balance increases yield and crop quality.'
                ),
                'duration': '22 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['nutrients', 'nitrogen', 'phosphorus', 'potassium', 'fertilizer'],
            },
            {
                'id': 'agri_003',
                'title': 'Crop Rotation and Sustainable Farming',
                'description': 'Explore crop rotation practices and sustainable agriculture methods',
                'content': (
                    'Crop rotation is the practice of planting different crops in the same area '
                    'in sequential seasons or years. Benefits include:\n\n'
                    '• Soil nutrient preservation (legumes fix nitrogen)\n'
                    '• Disease and pest control\n'
                    '• Improved soil structure and fertility\n'
                    '• Reduced need for chemical pesticides\n'
                    '• Better long-term farm productivity\n\n'
                    'Sustainable farming integrates:\n'
                    '• Soil conservation\n'
                    '• Water management\n'
                    '• Integrated pest management (IPM)\n'
                    '• Organic farming practices\n'
                    '• Conservation of biodiversity'
                ),
                'duration': '25 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['crop rotation', 'sustainability', 'legumes', 'organic farming'],
            },
            {
                'id': 'agri_004',
                'title': 'Irrigation and Water Management',
                'description': 'Master irrigation techniques and water conservation for farming',
                'content': (
                    'Water management is critical for agricultural success. Methods include:\n\n'
                    'Traditional Irrigation:\n'
                    '• Flood irrigation - water flows across fields\n'
                    '• Furrow irrigation - water runs along plant rows\n'
                    '• Overhead sprinklers - simulates rainfall\n\n'
                    'Modern Irrigation:\n'
                    '• Drip irrigation - delivers water directly to roots (most efficient)\n'
                    '• Micro-sprinklers - targeted water delivery\n'
                    '• Smart irrigation - sensor-based, automated systems\n\n'
                    'Key concepts:\n'
                    '• Water availability and seasons\n'
                    '• Soil water-holding capacity\n'
                    '• Evapotranspiration rates\n'
                    '• Conservation and sustainability'
                ),
                'duration': '23 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['irrigation', 'water management', 'drip irrigation', 'evapotranspiration'],
            },
            {
                'id': 'agri_005',
                'title': 'Pest and Disease Management',
                'description': 'Learn about crop protection and integrated pest management',
                'content': (
                    'Pests and diseases significantly reduce crop yields. Management strategies:\n\n'
                    'Integrated Pest Management (IPM):\n'
                    '• Prevention through crop selection and rotation\n'
                    '• Monitoring and early detection\n'
                    '• Cultural practices (pruning, sanitation)\n'
                    '• Biological control (predators, parasites)\n'
                    '• Chemical control (pesticides) as last resort\n\n'
                    'Common pests:\n'
                    '• Insects (locusts, aphids, beetles)\n'
                    '• Rodents and birds\n'
                    '• Nematodes\n\n'
                    'Plant diseases:\n'
                    '• Fungal (powdery mildew, rust)\n'
                    '• Bacterial (blight, wilt)\n'
                    '• Viral (mosaic, leaf curl)'
                ),
                'duration': '25 minutes',
                'difficulty': 'Advanced',
                'keywords': ['pest', 'disease', 'IPM', 'fungal', 'bacterial'],
            },
            {
                'id': 'agri_006',
                'title': 'Crop Breeding and Genetics',
                'description': 'Understand crop improvement through selective breeding and genetics',
                'content': (
                    'Modern agriculture relies on improved crop varieties through breeding programs:\n\n'
                    'Traditional Breeding:\n'
                    '• Selecting plants with desirable traits\n'
                    '• Cross-pollination and hybridization\n'
                    '• Multi-generational selection\n'
                    '• Produces 10-20% yield improvements\n\n'
                    'Genetic Engineering:\n'
                    '• Direct DNA modification\n'
                    '• Disease resistance genes\n'
                    '• Enhanced nutritional content\n'
                    '• Drought and stress tolerance\n\n'
                    'Breeding objectives:\n'
                    '• Higher yield\n'
                    '• Disease/pest resistance\n'
                    '• Better nutritional value\n'
                    '• Climate resilience\n'
                    '• Improved taste and appearance'
                ),
                'duration': '28 minutes',
                'difficulty': 'Advanced',
                'keywords': ['breeding', 'genetics', 'hybridization', 'GMO', 'yield'],
            },
            {
                'id': 'agri_007',
                'title': 'Machinery and Farm Technology',
                'description': 'Explore modern farm equipment and precision agriculture',
                'content': (
                    'Farm machinery has revolutionized agriculture by improving efficiency:\n\n'
                    'Traditional Equipment:\n'
                    '• Tractors - power source for field work\n'
                    '• Plows and tillers - soil preparation\n'
                    '• Harvesters - crop collection\n'
                    '• Threshers - grain separation\n\n'
                    'Precision Agriculture Technology:\n'
                    '• GPS-guided tractors - accurate field operations\n'
                    '• Drones - crop monitoring and spraying\n'
                    '• Sensors - soil and plant monitoring\n'
                    '• Variable rate technology - optimize input application\n\n'
                    'Benefits:\n'
                    '• Reduced labor costs\n'
                    '• Better timing of operations\n'
                    '• Optimized resource use\n'
                    '• Increased productivity and sustainability'
                ),
                'duration': '24 minutes',
                'difficulty': 'Advanced',
                'keywords': ['machinery', 'precision agriculture', 'GPS', 'drones', 'technology'],
            },
            {
                'id': 'agri_008',
                'title': 'Livestock and Animal Agriculture',
                'description': 'Learn about animal husbandry and livestock farming practices',
                'content': (
                    'Livestock production is a major component of agriculture:\n\n'
                    'Major Livestock Types:\n'
                    '• Cattle - beef and dairy\n'
                    '• Poultry - chickens, turkeys, ducks\n'
                    '• Swine - pork production\n'
                    '• Sheep - wool and meat\n'
                    '• Fish - aquaculture\n\n'
                    'Livestock Management:\n'
                    '• Nutrition and feed management\n'
                    '• Health and disease prevention\n'
                    '• Breeding for productivity\n'
                    '• Environmental management\n'
                    '• Welfare and ethical considerations\n\n'
                    'Production Systems:\n'
                    '• Intensive (high density, controlled environment)\n'
                    '• Extensive (pasture-based)\n'
                    '• Mixed farming (crops and livestock combined)'
                ),
                'duration': '26 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['livestock', 'cattle', 'poultry', 'aquaculture', 'husbandry'],
            },
            {
                'id': 'agri_009',
                'title': 'Post-Harvest Technology and Storage',
                'description': 'Understand crop preservation and post-harvest management',
                'content': (
                    'Post-harvest management prevents crop loss and maintains quality:\n\n'
                    'Harvesting Best Practices:\n'
                    '• Harvest at optimal maturity\n'
                    '• Minimize physical damage\n'
                    '• Quick cooling and field heat removal\n'
                    '• Proper handling during transport\n\n'
                    'Storage Methods:\n'
                    '• Cold storage - temperature control (0-15°C)\n'
                    '• Controlled atmosphere - reduced O2, increased CO2\n'
                    '• Drying - reduces moisture and extends shelf life\n'
                    '• Chemical preservation - fungicides, growth inhibitors\n\n'
                    'Value Addition:\n'
                    '• Processing (canning, freezing, drying)\n'
                    '• Packaging and branding\n'
                    '• Quality certification\n'
                    '• Market diversification'
                ),
                'duration': '22 minutes',
                'difficulty': 'Intermediate',
                'keywords': ['post-harvest', 'storage', 'preservation', 'processing', 'quality'],
            },
            {
                'id': 'agri_010',
                'title': 'Agricultural Economics and Marketing',
                'description': 'Learn about farm economics, pricing, and market strategies',
                'content': (
                    'Successful farming requires business acumen:\n\n'
                    'Farm Economics:\n'
                    '• Cost-benefit analysis\n'
                    '• Input costs (seeds, fertilizer, labor)\n'
                    '• Revenue from crop/livestock sales\n'
                    '• Profitability calculation\n'
                    '• Risk management and insurance\n\n'
                    'Market Factors:\n'
                    '• Supply and demand\n'
                    '• Seasonal price variations\n'
                    '• Quality and grading standards\n'
                    '• Export/import regulations\n\n'
                    'Marketing Strategies:\n'
                    '• Direct to consumer sales\n'
                    '• Wholesale markets\n'
                    '• Fair trade and organic certification\n'
                    '• Contract farming\n'
                    '• Value-added products'
                ),
                'duration': '24 minutes',
                'difficulty': 'Advanced',
                'keywords': ['economics', 'marketing', 'pricing', 'profit', 'market'],
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
            'Agricultural Science': AgricultureModule(),
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
