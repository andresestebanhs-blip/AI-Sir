import json
import random

# Categories and topics to generate
categories = {
    "history": [
        "Rome", "Egypt", "WWII", "Napoleon", "Maya", "Inca", "Aztec", "Greece", "Vikings", "Samurai",
        "Middle Ages", "Renaissance", "Industrial Revolution", "Cold War", "Civil War", "WWI", "Vietnam War",
        "Korean War", "Persian Empire", "Alexander the Great", "Julius Caesar", "Cleopatra", "Genghis Khan",
        "Ottoman Empire", "Byzantine Empire", "Holy Roman Empire", "French Revolution", "American Revolution",
        "Russian Revolution", "Ming Dynasty", "Han Dynasty", "Tang Dynasty", "Mughal Empire", "British Empire",
        "Spanish Empire", "Portuguese Empire", "Dutch Empire", "Belgian Empire", "Italian Empire", "German Empire",
        "Austro-Hungarian Empire", "Soviet Union", "Nazi Germany", "Fascist Italy", "Imperial Japan", "Feudalism",
        "Crusades", "Black Death", "Magna Carta", "Reformation", "Enlightenment", "Age of Discovery", "Colonialism",
        "Slavery", "Apartheid", "Civil Rights Movement", "Suffragettes", "Space Race", "Information Age", "Globalization"
    ],
    "science": [
        "Physics", "Chemistry", "Biology", "Astronomy", "Quantum Mechanics", "Evolution", "Genetics", "Robotics", "AI",
        "Nanotechnology", "Space Travel", "Black Holes", "Stars", "Planets", "Atoms", "Molecules", "Cells", "DNA",
        "RNA", "Bacteria", "Viruses", "Fungi", "Plants", "Animals", "Humans", "Brain", "Heart", "Lungs", "Liver",
        "Kidneys", "Stomach", "Intestines", "Bones", "Muscles", "Nerves", "Blood", "Immune System", "Cancer",
        "Diabetes", "Alzheimers", "Parkinsons", "Vaccines", "Antibiotics", "Anesthesia", "Surgery", "X-Rays", "MRI",
        "CT Scan", "Ultrasound", "Telescope", "Microscope", "Spectroscopy", "Chromatography", "Electrolysis",
        "Thermodynamics", "Relativity", "Gravity", "Magnetism", "Electricity", "Light", "Sound", "Heat", "Energy",
        "Force", "Motion", "Speed", "Velocity", "Acceleration", "Friction", "Inertia", "Momentum", "Work", "Power"
    ],
    "tech": [
        "Python", "Java", "C++", "Blockchain", "Internet", "Computers", "Smartphones", "VR", "AR", "Cybersecurity",
        "Cloud", "Big Data", "IoT", "5G", "Gaming", "Javascript", "HTML", "CSS", "React", "Angular", "Vue", "Nodejs",
        "Django", "Flask", "Spring", "Hibernate", "SQL", "NoSQL", "MongoDB", "PostgreSQL", "MySQL", "Oracle",
        "Microsoft", "Apple", "Google", "Amazon", "Facebook", "Twitter", "Instagram", "TikTok", "Snapchat", "LinkedIn",
        "YouTube", "Netflix", "Spotify", "Uber", "Airbnb", "Tesla", "SpaceX", "NASA", "ESA", "CERN", "Windows",
        "MacOS", "Linux", "Android", "iOS", "Hardware", "Software", "Firmware", "BIOS", "Motherboard", "CPU", "GPU",
        "RAM", "SSD", "HDD", "Monitor", "Keyboard", "Mouse", "Printer", "Router", "Switch", "Firewall", "Server"
    ],
    "geography": [
        "USA", "China", "Japan", "Russia", "Brazil", "Argentina", "Chile", "Europe", "Africa", "Asia", "Antarctica",
        "Oceans", "Mountains", "Rivers", "Volcanoes", "Canada", "Mexico", "Colombia", "Peru", "Venezuela", "Ecuador",
        "Bolivia", "Paraguay", "Uruguay", "UK", "France", "Germany", "Italy", "Spain", "Portugal", "Netherlands",
        "Belgium", "Switzerland", "Austria", "Poland", "Sweden", "Norway", "Denmark", "Finland", "Iceland", "Ireland",
        "Greece", "Turkey", "India", "Pakistan", "Bangladesh", "Thailand", "Vietnam", "Indonesia", "Malaysia",
        "Singapore", "Philippines", "Australia", "New Zealand", "Egypt", "South Africa", "Nigeria", "Kenya", "Morocco",
        "Saudi Arabia", "UAE", "Israel", "Iran", "Iraq", "Syria", "Lebanon", "Jordan", "Afghanistan", "Himalayas",
        "Andes", "Alps", "Rockies", "Amazon", "Nile", "Yangtze", "Mississippi", "Sahara", "Gobi", "Everest"
    ],
    "culture": [
        "Art", "Music", "Movies", "Literature", "Philosophy", "Religion", "Sports", "Football", "Basketball", "Cooking",
        "Fashion", "Architecture", "Dance", "Theater", "Painting", "Sculpture", "Photography", "Design", "Ballet",
        "Opera", "Jazz", "Rock", "Pop", "Hip Hop", "Classical", "Folk", "Blues", "Reggae", "Metal", "Punk", "Techno",
        "House", "Trance", "Dubstep", "Drum and Bass", "Ambient", "Cinema", "Hollywood", "Bollywood", "Anime", "Manga",
        "Comics", "Video Games", "Board Games", "Card Games", "Chess", "Poker", "Tennis", "Golf", "Swimming", "Running",
        "Cycling", "Boxing", "MMA", "Wrestling", "Karate", "Judo", "Taekwondo", "Kung Fu", "Yoga", "Meditation",
        "Buddhism", "Christianity", "Islam", "Judaism", "Hinduism", "Sikhism", "Taoism", "Confucianism", "Shinto"
    ],
    "nature": [
        "Trees", "Flowers", "Forests", "Deserts", "Oceans", "Lakes", "Rivers", "Mountains", "Rain", "Snow", "Wind",
        "Storms", "Lightning", "Thunder", "Clouds", "Sun", "Moon", "Stars", "Sky", "Earth", "Fire", "Water", "Air",
        "Soil", "Rocks", "Minerals", "Gems", "Gold", "Silver", "Diamond", "Ruby", "Emerald", "Sapphire", "Pearl",
        "Coral", "Fish", "Birds", "Insects", "Reptiles", "Mammals", "Amphibians", "Sharks", "Whales", "Dolphins",
        "Lions", "Tigers", "Bears", "Wolves", "Dogs", "Cats", "Horses", "Cows", "Pigs", "Sheep", "Goats", "Chickens"
    ],
    "concepts": [
        "Love", "Hate", "Peace", "War", "Freedom", "Justice", "Truth", "Lies", "Good", "Bad", "Right", "Wrong",
        "Happiness", "Sadness", "Anger", "Fear", "Hope", "Despair", "Life", "Death", "Time", "Space", "Matter",
        "Energy", "Reality", "Dreams", "Knowledge", "Ignorance", "Wisdom", "Stupidity", "Logic", "Emotion", "Mind",
        "Body", "Soul", "Spirit", "Consciousness", "Unconsciousness", "Memory", "Imagination", "Creativity", "Art",
        "Science", "Religion", "Philosophy", "Politics", "Economics", "Sociology", "Psychology", "History", "Geography"
    ]
}

# Butler-style templates
responses_templates = [
    "Aquí tiene la información solicitada sobre {topic}, señor.",
    "He recopilado los siguientes datos sobre {topic} para usted.",
    "Un tema fascinante, señor. Esto es lo que sé sobre {topic}.",
    "Permítame informarle sobre {topic}, señor.",
    "Por supuesto, señor. {topic} es un asunto de gran interés."
]

generated_intents = []

# Generate 500+ intents (using combinations to reach high numbers if needed, but here simple expansion)
# To actually reach 500 unique topics without an API is hard, so we will generate variants
# We will create specific specific sub-topics/questions for each main topic.

for category, topics in categories.items():
    for topic in topics:
        # Create standard informational intent
        intent = {
            "tag": f"info_{topic.lower().replace(' ', '_')}",
            "patterns": [
                f"Hablame de {topic}",
                f"Que sabes de {topic}?",
                f"Informacion sobre {topic}",
                f"Quien fue {topic}?",
                f"Dime cosas sobre {topic}",
                f"{topic}"
            ],
            "responses": [
                template.format(topic=topic) for template in responses_templates
            ]
        }
        generated_intents.append(intent)

# Load existing intents
with open('intents.json', 'r') as f:
    data = json.load(f)

# Update existing intents to Alfred persona (Manual override for core intents)
for intent in data['intents']:
    if intent['tag'] == 'greeting':
        intent['responses'] = [
            "Buenos días, señor. ¿En qué puedo servirle?",
            "Bienvenido. Sus sistemas están listos.",
            "Hola, señor. AI-Sir a la espera de sus órdenes."
        ]
    elif intent['tag'] == 'goodbye':
        intent['responses'] = [
            "Hasta la vista, señor. Cuídese.",
            "Desconectando sistemas centrales. Que tenga buen día.",
            "Ha sido un placer servirle, señor."
        ]
    elif intent['tag'] == 'thanks':
        intent['responses'] = [
            "Es un honor servirle, señor.",
            "No hay de qué, señor.",
            "Simplemente cumplo con mi deber."
        ]
    elif intent['tag'] == 'identity':
        intent['responses'] = [
            "Soy AI-Sir, su leal asistente virtual.",
            "Me llamo AI-Sir, estoy aquí para facilitar su vida, señor."
        ]

# Append generated intents
# Filter to avoid duplicates if re-run
existing_tags = [i['tag'] for i in data['intents']]
for new_intent in generated_intents:
    if new_intent['tag'] not in existing_tags:
        data['intents'].append(new_intent)

# Save back
with open('intents.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Successfully generated {len(generated_intents)} new topics and updated persona.")
print(f"Total intents: {len(data['intents'])}")
