"""Agricultural Science Curriculum Module - Farm and crop education content"""

from typing import Dict, List

class AgricultureModule:
    """Agricultural Science curriculum module"""
    
    def __init__(self):
        self.name = 'Agricultural Science'
        self.subject = 'Agricultural Science'
        self.level = 'All Levels'
        self.lessons = []
        self.quizzes = []
        self._initialize_lessons()
    
    def add_lesson(self, lesson: Dict):
        """Add a lesson to the module"""
        self.lessons.append(lesson)
    
    def get_lessons(self) -> List[Dict]:
        """Get all lessons in the module"""
        return self.lessons
    
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


class AgricultureSubtopics:
    """Detailed subtopics within agricultural science"""
    
    CROP_TYPES = {
        'Cereals': ['Wheat', 'Rice', 'Corn', 'Barley', 'Oats'],
        'Legumes': ['Beans', 'Peas', 'Lentils', 'Chickpeas', 'Soybeans'],
        'Vegetables': ['Tomatoes', 'Potatoes', 'Carrots', 'Cabbage', 'Lettuce'],
        'Fruits': ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Mangoes'],
        'Oil Crops': ['Sunflower', 'Rapeseed', 'Coconut', 'Palm', 'Peanut'],
        'Cash Crops': ['Cotton', 'Sugar Cane', 'Tobacco', 'Coffee', 'Tea'],
    }
    
    FARMING_METHODS = {
        'Traditional Farming': {
            'description': 'Manual labor-based farming',
            'tools': ['Hoe', 'Spade', 'Machete', 'Manual pump'],
            'advantages': 'Low input costs, sustainable',
            'disadvantages': 'High labor, low productivity',
        },
        'Conventional Farming': {
            'description': 'Mechanized farming with chemical inputs',
            'tools': ['Tractor', 'Combine harvester', 'Sprayers'],
            'advantages': 'High productivity, lower labor',
            'disadvantages': 'High input costs, environmental concerns',
        },
        'Organic Farming': {
            'description': 'No synthetic chemicals, natural inputs',
            'tools': ['Compost', 'Biopesticides', 'Green manure'],
            'advantages': 'Sustainable, premium prices',
            'disadvantages': 'Lower yields, labor intensive',
        },
        'Conservation Agriculture': {
            'description': 'Minimal soil disturbance, cover crops',
            'tools': ['No-till planter', 'Cover crop seeder'],
            'advantages': 'Soil conservation, reduced erosion',
            'disadvantages': 'Requires expertise',
        },
    }
    
    CLIMATE_FACTORS = {
        'Temperature': {
            'optimal_range': '15-30°C for most crops',
            'importance': 'Affects germination, growth, and maturity',
            'management': 'Crop selection, timing, greenhouse farming',
        },
        'Rainfall': {
            'optimal_range': '400-2000mm annually',
            'importance': 'Primary water source for crops',
            'management': 'Irrigation, water harvesting, mulching',
        },
        'Humidity': {
            'optimal_range': '40-80% for most crops',
            'importance': 'Affects transpiration and disease',
            'management': 'Proper spacing, ventilation, fungicide use',
        },
        'Sunlight': {
            'optimal_range': '10-16 hours for most crops',
            'importance': 'Energy source for photosynthesis',
            'management': 'Intercropping, row orientation, pruning',
        },
    }

    @staticmethod
    def get_crop_varieties(crop_type: str) -> List[str]:
        """Get varieties for a specific crop type"""
        return AgricultureSubtopics.CROP_TYPES.get(crop_type, [])
    
    @staticmethod
    def get_farming_method_details(method: str) -> Dict:
        """Get details about a specific farming method"""
        return AgricultureSubtopics.FARMING_METHODS.get(method, {})
    
    @staticmethod
    def get_climate_requirements(factor: str) -> Dict:
        """Get climate requirements for farming"""
        return AgricultureSubtopics.CLIMATE_FACTORS.get(factor, {})
