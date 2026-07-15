"""Agricultural Science Quizzes - Assessment and learning evaluation"""

from typing import Dict, List

class AgriculturalQuiz:
    """Quiz management for agricultural science topics"""
    
    def __init__(self):
        self.quizzes = {}
        self._initialize_quizzes()
    
    def _initialize_quizzes(self):
        """Initialize all agricultural science quizzes"""
        
        # Soil Composition Quiz
        self.quizzes['soil_composition'] = {
            'id': 'agri_quiz_001',
            'topic': 'Soil Composition and Properties',
            'difficulty': 'Beginner',
            'duration': '10 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What are the three main mineral components of soil?',
                    'type': 'multiple_choice',
                    'options': [
                        'Sand, Silt, and Clay',
                        'Gravel, Silt, and Peat',
                        'Sand, Rock, and Mineral',
                        'Clay, Loam, and Stone'
                    ],
                    'correct_answer': 'Sand, Silt, and Clay',
                    'explanation': 'Soil composition is determined by the proportion of sand, silt, and clay particles. This ratio determines soil texture and its agricultural properties.'
                },
                {
                    'id': 'q2',
                    'question': 'What does soil pH affect in farming?',
                    'type': 'multiple_choice',
                    'options': [
                        'Only plant color',
                        'Nutrient availability and microbial activity',
                        'Rainfall patterns',
                        'Climate temperature'
                    ],
                    'correct_answer': 'Nutrient availability and microbial activity',
                    'explanation': 'Soil pH (acidity/alkalinity) critically affects which nutrients are available to plants and the activity of beneficial soil microorganisms.'
                },
                {
                    'id': 'q3',
                    'question': 'Which soil type has the best water retention?',
                    'type': 'multiple_choice',
                    'options': [
                        'Sandy soil',
                        'Clay soil',
                        'Gravelly soil',
                        'Rocky soil'
                    ],
                    'correct_answer': 'Clay soil',
                    'explanation': 'Clay soil has the smallest particles, providing excellent water retention but poor drainage. It requires careful management to avoid waterlogging.'
                },
                {
                    'id': 'q4',
                    'question': 'True or False: Organic matter in soil improves its structure and fertility.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Organic matter (decomposed plants and animals) improves soil structure, increases water retention, and provides nutrients for plant growth.'
                },
                {
                    'id': 'q5',
                    'question': 'What is the ideal soil pH range for most crops?',
                    'type': 'multiple_choice',
                    'options': [
                        '2-4 (very acidic)',
                        '6-7 (neutral to slightly acidic)',
                        '8-9 (alkaline)',
                        '10-12 (very alkaline)'
                    ],
                    'correct_answer': '6-7 (neutral to slightly acidic)',
                    'explanation': 'Most crops thrive in soil with a pH between 6-7, where nutrients are most available to plant roots.'
                }
            ]
        }
        
        # Plant Nutrition Quiz
        self.quizzes['plant_nutrition'] = {
            'id': 'agri_quiz_002',
            'topic': 'Plant Nutrition and Fertilizers',
            'difficulty': 'Intermediate',
            'duration': '12 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What does the "N" in NPK fertilizer stand for?',
                    'type': 'multiple_choice',
                    'options': [
                        'Neon',
                        'Nitrogen',
                        'Nickel',
                        'Neon'
                    ],
                    'correct_answer': 'Nitrogen',
                    'explanation': 'N stands for Nitrogen, which promotes leaf and stem growth in plants.'
                },
                {
                    'id': 'q2',
                    'question': 'How many essential nutrients do plants need?',
                    'type': 'multiple_choice',
                    'options': [
                        '6 nutrients',
                        '10 nutrients',
                        '16 nutrients',
                        '20 nutrients'
                    ],
                    'correct_answer': '16 nutrients',
                    'explanation': 'Plants require 16 essential nutrients: 3 macronutrients (C, H, O from air/water), and 13 from soil (N, P, K, Ca, Mg, S, Fe, Zn, Cu, B, Mo, Mn, Cl).'
                },
                {
                    'id': 'q3',
                    'question': 'What is the primary role of Phosphorus (P) in plants?',
                    'type': 'multiple_choice',
                    'options': [
                        'Leaf growth and color',
                        'Root development and flowering',
                        'Seed germination only',
                        'Disease resistance only'
                    ],
                    'correct_answer': 'Root development and flowering',
                    'explanation': 'Phosphorus promotes strong root systems and is essential for flowering and seed production.'
                },
                {
                    'id': 'q4',
                    'question': 'Which type of fertilizer is better for long-term soil health?',
                    'type': 'multiple_choice',
                    'options': [
                        'Synthetic fertilizers only',
                        'Organic fertilizers (compost, manure)',
                        'Chemical pesticides',
                        'Salt-based fertilizers'
                    ],
                    'correct_answer': 'Organic fertilizers (compost, manure)',
                    'explanation': 'Organic fertilizers improve soil structure and microbial life while synthetic fertilizers provide quick nutrients but can degrade soil health long-term.'
                },
                {
                    'id': 'q5',
                    'question': 'What are micronutrients?',
                    'type': 'multiple_choice',
                    'options': [
                        'Nutrients plants need in large quantities',
                        'Nutrients plants need in small quantities',
                        'Nutrients found only in water',
                        'Nutrients that harm plants'
                    ],
                    'correct_answer': 'Nutrients plants need in small quantities',
                    'explanation': 'Micronutrients like Iron, Zinc, and Copper are needed in small amounts but are essential for plant metabolism and growth.'
                }
            ]
        }
        
        # Crop Rotation Quiz
        self.quizzes['crop_rotation'] = {
            'id': 'agri_quiz_003',
            'topic': 'Crop Rotation and Sustainable Farming',
            'difficulty': 'Intermediate',
            'duration': '12 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What is the primary benefit of crop rotation?',
                    'type': 'multiple_choice',
                    'options': [
                        'Increase pesticide use',
                        'Reduce soil nutrient depletion and pest buildup',
                        'Grow only one crop type',
                        'Decrease water usage'
                    ],
                    'correct_answer': 'Reduce soil nutrient depletion and pest buildup',
                    'explanation': 'Crop rotation helps maintain soil fertility, breaks pest cycles, and improves long-term farm productivity.'
                },
                {
                    'id': 'q2',
                    'question': 'Which crop type helps fix nitrogen in the soil?',
                    'type': 'multiple_choice',
                    'options': [
                        'Grains (wheat, corn)',
                        'Legumes (beans, peas, alfalfa)',
                        'Root vegetables',
                        'Fruits'
                    ],
                    'correct_answer': 'Legumes (beans, peas, alfalfa)',
                    'explanation': 'Legumes have nitrogen-fixing bacteria in their root nodules that convert atmospheric nitrogen into soil nitrogen, enriching the soil naturally.'
                },
                {
                    'id': 'q3',
                    'question': 'True or False: Sustainable farming practices include water conservation and biodiversity preservation.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Sustainable farming integrates environmental protection, soil conservation, water management, and biodiversity preservation for long-term productivity.'
                },
                {
                    'id': 'q4',
                    'question': 'What is a cover crop?',
                    'type': 'multiple_choice',
                    'options': [
                        'A crop that covers the entire field',
                        'A temporary crop planted to protect and enrich soil',
                        'A crop used only for decoration',
                        'A crop that requires no water'
                    ],
                    'correct_answer': 'A temporary crop planted to protect and enrich soil',
                    'explanation': 'Cover crops like clover or rye are planted off-season to prevent erosion, fix nitrogen, and improve soil structure.'
                },
                {
                    'id': 'q5',
                    'question': 'How does crop rotation reduce pest problems?',
                    'type': 'multiple_choice',
                    'options': [
                        'Pests cannot fly to new fields',
                        'Different crops host different pests, breaking pest cycles',
                        'All pests die in winter',
                        'It does not reduce pest problems'
                    ],
                    'correct_answer': 'Different crops host different pests, breaking pest cycles',
                    'explanation': 'Crop rotation interrupts pest life cycles because pests specific to one crop cannot survive on unrelated crops, reducing pest populations naturally.'
                }
            ]
        }
        
        # Irrigation Quiz
        self.quizzes['irrigation'] = {
            'id': 'agri_quiz_004',
            'topic': 'Irrigation and Water Management',
            'difficulty': 'Intermediate',
            'duration': '11 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'Which irrigation method is most water-efficient?',
                    'type': 'multiple_choice',
                    'options': [
                        'Flood irrigation',
                        'Drip irrigation',
                        'Overhead sprinklers',
                        'Furrow irrigation'
                    ],
                    'correct_answer': 'Drip irrigation',
                    'explanation': 'Drip irrigation delivers water directly to plant roots with 90%+ efficiency, minimizing water loss through evaporation and runoff.'
                },
                {
                    'id': 'q2',
                    'question': 'What does evapotranspiration (ET) refer to?',
                    'type': 'multiple_choice',
                    'options': [
                        'Water absorbed by roots only',
                        'Soil water drainage only',
                        'Water lost through soil evaporation and plant transpiration',
                        'Rainfall measurement'
                    ],
                    'correct_answer': 'Water lost through soil evaporation and plant transpiration',
                    'explanation': 'Evapotranspiration is the combined water loss from soil surface evaporation and plant leaf transpiration, important for irrigation planning.'
                },
                {
                    'id': 'q3',
                    'question': 'Which traditional irrigation method is still commonly used due to low cost?',
                    'type': 'multiple_choice',
                    'options': [
                        'Hydroponics',
                        'Flood/furrow irrigation',
                        'Aerial irrigation',
                        'Subsurface irrigation'
                    ],
                    'correct_answer': 'Flood/furrow irrigation',
                    'explanation': 'Flood and furrow irrigation remain popular in developing regions due to low infrastructure costs, though they are less water-efficient.'
                },
                {
                    'id': 'q4',
                    'question': 'What is the advantage of smart irrigation systems?',
                    'type': 'multiple_choice',
                    'options': [
                        'They require more water',
                        'They use soil sensors to optimize water delivery based on actual needs',
                        'They eliminate the need for fertilizer',
                        'They prevent all plant diseases'
                    ],
                    'correct_answer': 'They use soil sensors to optimize water delivery based on actual needs',
                    'explanation': 'Smart irrigation systems use moisture sensors and weather data to apply water only when needed, reducing waste and improving crop yield.'
                },
                {
                    'id': 'q5',
                    'question': 'True or False: Different soil types have the same water-holding capacity.',
                    'type': 'true_false',
                    'correct_answer': False,
                    'explanation': 'Clay soils hold more water than sandy soils. Understanding soil water-holding capacity is crucial for proper irrigation scheduling.'
                }
            ]
        }
        
        # Pest Management Quiz
        self.quizzes['pest_management'] = {
            'id': 'agri_quiz_005',
            'topic': 'Pest and Disease Management',
            'difficulty': 'Advanced',
            'duration': '13 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What does IPM (Integrated Pest Management) prioritize?',
                    'type': 'multiple_choice',
                    'options': [
                        'Using pesticides immediately',
                        'Prevention, monitoring, biological control, then chemical control as last resort',
                        'Growing single crops only',
                        'Accepting all crop losses'
                    ],
                    'correct_answer': 'Prevention, monitoring, biological control, then chemical control as last resort',
                    'explanation': 'IPM uses a multi-strategy approach: prevention through crop selection/rotation, early detection, biological controls, and chemicals only when necessary.'
                },
                {
                    'id': 'q2',
                    'question': 'Which is an example of biological pest control?',
                    'type': 'multiple_choice',
                    'options': [
                        'Spraying insecticide',
                        'Introducing ladybugs to control aphids',
                        'Removing all plants',
                        'Using salt to kill pests'
                    ],
                    'correct_answer': 'Introducing ladybugs to control aphids',
                    'explanation': 'Biological control uses natural predators or parasites to control pests, reducing chemical pesticide dependence.'
                },
                {
                    'id': 'q3',
                    'question': 'What are the three main types of plant diseases?',
                    'type': 'multiple_choice',
                    'options': [
                        'Bacterial, Chemical, and Physical',
                        'Fungal, Bacterial, and Viral',
                        'Insect, Animal, and Plant',
                        'Soil, Water, and Air'
                    ],
                    'correct_answer': 'Fungal, Bacterial, and Viral',
                    'explanation': 'Plant diseases are typically caused by fungi (powdery mildew, rust), bacteria (blight, wilt), or viruses (mosaic, leaf curl).'
                },
                {
                    'id': 'q4',
                    'question': 'What is the first step in pest monitoring?',
                    'type': 'multiple_choice',
                    'options': [
                        'Apply pesticides immediately',
                        'Pull out infected plants',
                        'Scout fields regularly to identify pests early',
                        'Wait for visible crop damage'
                    ],
                    'correct_answer': 'Scout fields regularly to identify pests early',
                    'explanation': 'Regular field scouting allows early detection of pests before they cause significant damage, enabling timely and appropriate responses.'
                },
                {
                    'id': 'q5',
                    'question': 'True or False: Pesticide resistance can develop in pest populations over time.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Repeated pesticide use can select for resistant pest populations, making chemicals less effective over time. This is why IPM and crop rotation are important.'
                }
            ]
        }
        
        # Crop Breeding Quiz
        self.quizzes['crop_breeding'] = {
            'id': 'agri_quiz_006',
            'topic': 'Crop Breeding and Genetics',
            'difficulty': 'Advanced',
            'duration': '13 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What is the goal of crop breeding?',
                    'type': 'multiple_choice',
                    'options': [
                        'To grow only one type of crop',
                        'To improve crop yield, quality, disease resistance, and adaptability',
                        'To eliminate all crop varieties',
                        'To increase pesticide use'
                    ],
                    'correct_answer': 'To improve crop yield, quality, disease resistance, and adaptability',
                    'explanation': 'Crop breeding aims to develop varieties with higher yields, better nutrition, disease/pest resistance, and climate resilience.'
                },
                {
                    'id': 'q2',
                    'question': 'What is hybridization in crop breeding?',
                    'type': 'multiple_choice',
                    'options': [
                        'Mixing soil types',
                        'Crossbreeding different plant varieties to combine desirable traits',
                        'Adding chemicals to seeds',
                        'Growing plants in water'
                    ],
                    'correct_answer': 'Crossbreeding different plant varieties to combine desirable traits',
                    'explanation': 'Hybridization crosses two different plant varieties to produce offspring with combined desirable characteristics.'
                },
                {
                    'id': 'q3',
                    'question': 'How much yield improvement can traditional breeding provide?',
                    'type': 'multiple_choice',
                    'options': [
                        '1-5% improvement',
                        '10-20% improvement',
                        '50% improvement',
                        '100% improvement'
                    ],
                    'correct_answer': '10-20% improvement',
                    'explanation': 'Traditional selective breeding typically produces 10-20% yield improvements over several generations through careful selection of parent plants.'
                },
                {
                    'id': 'q4',
                    'question': 'What is genetic engineering in agriculture?',
                    'type': 'multiple_choice',
                    'options': [
                        'Selecting seeds manually',
                        'Direct manipulation of plant DNA to introduce desired traits',
                        'Watering plants more frequently',
                        'Using only organic methods'
                    ],
                    'correct_answer': 'Direct manipulation of plant DNA to introduce desired traits',
                    'explanation': 'Genetic engineering directly modifies plant DNA to introduce specific genes for traits like disease resistance, drought tolerance, or enhanced nutrition.'
                },
                {
                    'id': 'q5',
                    'question': 'True or False: Climate-resilient crop varieties are being developed to handle drought and extreme weather.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Modern breeding programs focus on developing varieties that can withstand drought, floods, heat stress, and other climate challenges to ensure food security.'
                }
            ]
        }
        
        # Farm Technology Quiz
        self.quizzes['farm_technology'] = {
            'id': 'agri_quiz_007',
            'topic': 'Machinery and Farm Technology',
            'difficulty': 'Advanced',
            'duration': '12 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What is precision agriculture?',
                    'type': 'multiple_choice',
                    'options': [
                        'Farming by hand only',
                        'Using technology to optimize field operations, reduce inputs, and increase yields',
                        'Large-scale monoculture farming',
                        'Farming without any machinery'
                    ],
                    'correct_answer': 'Using technology to optimize field operations, reduce inputs, and increase yields',
                    'explanation': 'Precision agriculture uses GPS, sensors, drones, and data analysis to optimize planting, fertilizing, and harvesting decisions.'
                },
                {
                    'id': 'q2',
                    'question': 'What is the advantage of GPS-guided tractors?',
                    'type': 'multiple_choice',
                    'options': [
                        'They reduce the need for fuel',
                        'They eliminate the need for farmers',
                        'They enable accurate field operations, reducing overlap and input waste',
                        'They prevent all crop diseases'
                    ],
                    'correct_answer': 'They enable accurate field operations, reducing overlap and input waste',
                    'explanation': 'GPS-guided tractors follow precise paths, reducing overlap in planting and fertilizing, which saves inputs and improves efficiency.'
                },
                {
                    'id': 'q3',
                    'question': 'What can agricultural drones be used for?',
                    'type': 'multiple_choice',
                    'options': [
                        'Crop monitoring and spraying only',
                        'Monitoring crop health, detecting pests/diseases, spraying, and collecting data',
                        'Harvesting crops only',
                        'Measuring rainfall only'
                    ],
                    'correct_answer': 'Monitoring crop health, detecting pests/diseases, spraying, and collecting data',
                    'explanation': 'Modern agricultural drones can monitor crop health via multispectral imaging, detect problems early, apply inputs precisely, and collect field data.'
                },
                {
                    'id': 'q4',
                    'question': 'What is variable rate technology (VRT)?',
                    'type': 'multiple_choice',
                    'options': [
                        'Changing tractor speeds randomly',
                        'Varying fertilizer application rates based on field variability and crop needs',
                        'Rotating crop types monthly',
                        'Changing irrigation schedules weekly'
                    ],
                    'correct_answer': 'Varying fertilizer application rates based on field variability and crop needs',
                    'explanation': 'VRT applies different rates of seeds, fertilizer, or pesticides to different field areas based on soil conditions and plant needs, optimizing inputs.'
                },
                {
                    'id': 'q5',
                    'question': 'True or False: Farm technology reduces labor requirements and improves productivity.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Modern farm machinery and technology significantly reduce labor needs, improve timeliness of operations, and increase overall farm productivity.'
                }
            ]
        }
        
        # Livestock Quiz
        self.quizzes['livestock'] = {
            'id': 'agri_quiz_008',
            'topic': 'Livestock and Animal Agriculture',
            'difficulty': 'Intermediate',
            'duration': '11 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What are the main livestock types?',
                    'type': 'multiple_choice',
                    'options': [
                        'Only cattle',
                        'Cattle, poultry, swine, sheep, and fish (aquaculture)',
                        'Only chickens',
                        'Wild animals'
                    ],
                    'correct_answer': 'Cattle, poultry, swine, sheep, and fish (aquaculture)',
                    'explanation': 'Major livestock production includes beef/dairy cattle, poultry (chickens, turkeys, ducks), swine, sheep, and aquaculture (fish and shellfish).'
                },
                {
                    'id': 'q2',
                    'question': 'What does intensive livestock production mean?',
                    'type': 'multiple_choice',
                    'options': [
                        'Animals raised only in open fields',
                        'High density, controlled environment systems with efficient feed conversion',
                        'Animals kept in small groups',
                        'Organic farming only'
                    ],
                    'correct_answer': 'High density, controlled environment systems with efficient feed conversion',
                    'explanation': 'Intensive systems maximize production efficiency with controlled environments, but require careful management of animal health and environmental impact.'
                },
                {
                    'id': 'q3',
                    'question': 'What is the primary focus of livestock nutrition management?',
                    'type': 'multiple_choice',
                    'options': [
                        'Feeding animals random food',
                        'Providing balanced diets that meet nutritional requirements and optimize growth',
                        'Feeding only grass',
                        'Minimizing food costs regardless of nutrition'
                    ],
                    'correct_answer': 'Providing balanced diets that meet nutritional requirements and optimize growth',
                    'explanation': 'Proper livestock nutrition requires balanced diets with appropriate protein, energy, minerals, and vitamins for health and productivity.'
                },
                {
                    'id': 'q4',
                    'question': 'What is extensive livestock production?',
                    'type': 'multiple_choice',
                    'options': [
                        'Very large farms only',
                        'Pasture-based systems with animals grazing on natural vegetation',
                        'Animals kept in buildings permanently',
                        'Using chemicals extensively'
                    ],
                    'correct_answer': 'Pasture-based systems with animals grazing on natural vegetation',
                    'explanation': 'Extensive production relies on natural pasture grazing, resulting in lower production intensity but often better animal welfare and environmental outcomes.'
                },
                {
                    'id': 'q5',
                    'question': 'True or False: Animal breeding can improve productivity and disease resistance.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Selective breeding of livestock improves traits like growth rate, milk production, meat quality, and resistance to diseases.'
                }
            ]
        }
        
        # Post-Harvest Quiz
        self.quizzes['post_harvest'] = {
            'id': 'agri_quiz_009',
            'topic': 'Post-Harvest Technology and Storage',
            'difficulty': 'Intermediate',
            'duration': '11 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What is the primary goal of post-harvest management?',
                    'type': 'multiple_choice',
                    'options': [
                        'To increase crop weight',
                        'To prevent crop loss and maintain quality from harvest to consumer',
                        'To add artificial colors',
                        'To reduce crop size'
                    ],
                    'correct_answer': 'To prevent crop loss and maintain quality from harvest to consumer',
                    'explanation': 'Post-harvest management minimizes losses due to spoilage, maintains nutritional value, and ensures food safety and quality.'
                },
                {
                    'id': 'q2',
                    'question': 'Why is quick cooling important after harvest?',
                    'type': 'multiple_choice',
                    'options': [
                        'It wastes energy',
                        'It slows respiration and microbial growth, extending shelf life',
                        'It makes crops heavier',
                        'It is not important'
                    ],
                    'correct_answer': 'It slows respiration and microbial growth, extending shelf life',
                    'explanation': 'Removing field heat quickly after harvest dramatically extends shelf life by slowing plant respiration and microbial spoilage.'
                },
                {
                    'id': 'q3',
                    'question': 'Which storage method is best for long-term preservation?',
                    'type': 'multiple_choice',
                    'options': [
                        'Leaving crops in the sun',
                        'Cold storage with controlled temperature and humidity',
                        'Storing in warm places',
                        'No storage needed'
                    ],
                    'correct_answer': 'Cold storage with controlled temperature and humidity',
                    'explanation': 'Cold storage (0-15°C) with controlled humidity maintains crop quality and extends storage life by slowing respiration and microbial activity.'
                },
                {
                    'id': 'q4',
                    'question': 'What is value addition in agriculture?',
                    'type': 'multiple_choice',
                    'options': [
                        'Selling raw crops at market prices',
                        'Processing crops into higher-value products (canning, freezing, drying)',
                        'Throwing away damaged crops',
                        'Growing only one crop type'
                    ],
                    'correct_answer': 'Processing crops into higher-value products (canning, freezing, drying)',
                    'explanation': 'Value addition through processing, packaging, and branding increases profit margins and market opportunities for farmers.'
                },
                {
                    'id': 'q5',
                    'question': 'True or False: Controlled atmosphere storage can extend crop shelf life by days to months.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Controlled atmosphere storage reduces oxygen and increases CO2, dramatically slowing respiration and extending shelf life from weeks to months.'
                }
            ]
        }
        
        # Agricultural Economics Quiz
        self.quizzes['ag_economics'] = {
            'id': 'agri_quiz_010',
            'topic': 'Agricultural Economics and Marketing',
            'difficulty': 'Advanced',
            'duration': '13 minutes',
            'questions': [
                {
                    'id': 'q1',
                    'question': 'What is included in farm input costs?',
                    'type': 'multiple_choice',
                    'options': [
                        'Only seeds',
                        'Seeds, fertilizer, pesticides, labor, machinery, and fuel',
                        'Only machinery',
                        'Only labor'
                    ],
                    'correct_answer': 'Seeds, fertilizer, pesticides, labor, machinery, and fuel',
                    'explanation': 'Input costs include all expenses for production: seeds, fertilizers, pesticides, labor, machinery maintenance, fuel, and utilities.'
                },
                {
                    'id': 'q2',
                    'question': 'How does seasonal variation affect agricultural prices?',
                    'type': 'multiple_choice',
                    'options': [
                        'Prices stay the same year-round',
                        'Prices are highest at harvest (supply up) and lowest off-season (supply down)',
                        'Prices are lowest at harvest and highest off-season',
                        'Season does not affect prices'
                    ],
                    'correct_answer': 'Prices are lowest at harvest and highest off-season',
                    'explanation': 'Agricultural commodity prices typically drop at harvest when supply is highest and increase during off-season when supply is limited.'
                },
                {
                    'id': 'q3',
                    'question': 'What is organic certification?',
                    'type': 'multiple_choice',
                    'options': [
                        'Any farm can claim to be organic',
                        'Official verification that crops are grown without synthetic chemicals, fetching premium prices',
                        'A requirement for all farms',
                        'Not important for marketing'
                    ],
                    'correct_answer': 'Official verification that crops are grown without synthetic chemicals, fetching premium prices',
                    'explanation': 'Organic certification provides official verification and allows farmers to command premium prices in specialty markets.'
                },
                {
                    'id': 'q4',
                    'question': 'What is contract farming?',
                    'type': 'multiple_choice',
                    'options': [
                        'Farming without any agreements',
                        'Pre-arranged agreements guaranteeing purchase price and quantity before planting',
                        'Selling only to neighbors',
                        'Farming without planning'
                    ],
                    'correct_answer': 'Pre-arranged agreements guaranteeing purchase price and quantity before planting',
                    'explanation': 'Contract farming provides price certainty and market security, reducing farmer risk but potentially limiting autonomy.'
                },
                {
                    'id': 'q5',
                    'question': 'True or False: Direct-to-consumer marketing can increase farmer profits by eliminating middlemen.',
                    'type': 'true_false',
                    'correct_answer': True,
                    'explanation': 'Direct sales through farmers markets or CSA programs allow farmers to keep higher margins, though they require more marketing effort.'
                }
            ]
        }
    
    def get_quiz(self, quiz_name: str) -> Dict:
        """Get a specific quiz"""
        return self.quizzes.get(quiz_name)
    
    def get_all_quizzes(self) -> Dict:
        """Get all quizzes"""
        return self.quizzes
    
    def get_quiz_by_topic(self, topic: str) -> Dict:
        """Search quiz by topic name"""
        for quiz_name, quiz in self.quizzes.items():
            if topic.lower() in quiz['topic'].lower():
                return quiz
        return None
    
    def evaluate_answer(self, quiz_name: str, question_id: str, user_answer: str) -> Dict:
        """Evaluate student answer"""
        quiz = self.quizzes.get(quiz_name)
        if not quiz:
            return {'error': 'Quiz not found'}
        
        question = None
        for q in quiz['questions']:
            if q['id'] == question_id:
                question = q
                break
        
        if not question:
            return {'error': 'Question not found'}
        
        is_correct = (
            str(user_answer).lower() == str(question['correct_answer']).lower()
        )
        
        return {
            'is_correct': is_correct,
            'correct_answer': question['correct_answer'],
            'explanation': question['explanation'],
            'xp_earned': 15 if is_correct else 5,
        }
    
    def calculate_quiz_score(self, quiz_name: str, answers: Dict[str, str]) -> Dict:
        """Calculate overall quiz score"""
        quiz = self.quizzes.get(quiz_name)
        if not quiz:
            return {'error': 'Quiz not found'}
        
        correct = 0
        total = len(quiz['questions'])
        xp_earned = 0
        
        for question_id, user_answer in answers.items():
            evaluation = self.evaluate_answer(quiz_name, question_id, user_answer)
            if evaluation.get('is_correct'):
                correct += 1
                xp_earned += 15
            else:
                xp_earned += 5
        
        percentage = (correct / total * 100) if total > 0 else 0
        
        return {
            'quiz_name': quiz['topic'],
            'score': f"{correct}/{total}",
            'percentage': f"{percentage:.1f}%",
            'total_xp': xp_earned,
            'performance': self._get_performance_level(percentage),
        }
    
    def _get_performance_level(self, percentage: float) -> str:
        """Determine performance level based on percentage"""
        if percentage >= 90:
            return 'Excellent! 🌟'
        elif percentage >= 75:
            return 'Good! 👍'
        elif percentage >= 60:
            return 'Satisfactory 📚'
        elif percentage >= 40:
            return 'Needs Improvement 📖'
        else:
            return 'Review Required ⚠️'
