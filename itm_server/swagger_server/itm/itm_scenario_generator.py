import time
import uuid
import random

from swagger_server.models.scenario import Scenario
from swagger_server.models.environment import Environment
from swagger_server.models.patient import Patient
from swagger_server.models.vitals import Vitals
from swagger_server.models.medical_supply import MedicalSupply
from swagger_server.models.triage_category import TriageCategory

DESCRIPTIONS = [
    'Bomb blast at a concert venue causing chaos and injuries',
    'Explosion at a crowded marketplace causing mass casualties',
    'High-speed car crash resulting in multiple severe injuries',
    'Industrial fire causing injuries and smoke inhalation',
    'Major earthquake leading to collapsed structures and trapped individuals',
    'Massive building collapse with trapped individuals',
    'Mass shooting at a public event with numerous injured',
    'Multiple gunshot victims in a school shooting incident',
    'Terrorist attack involving chemical exposure in a subway station',
    'Train derailment with multiple casualties and trapped passengers'
]

FEMALE_FIRST_NAMES = [
    'Amanda', 'Betty', 'Carol', 'Dorothy', 'Emily', 'Jennifer', 'Jessica',
    'Karen', 'Kimberly', 'Linda', 'Lisa', 'Margaret', 'Mary', 'Melissa',
    'Michelle', 'Nancy', 'Patricia', 'Sarah', 'Susan'
]

INJURIES = [
    'Bilateral leg fractures', 'Chest gunshot wound', 'Foot crush injury',
    'Groin trauma', 'Hand laceration', 'Head trauma', 'Left ear damage',
    'Left shoulder dislocation', 'Neck fracture',
    'Penetrating abdominal trauma', 'Pelvic injury',
    'Right arm gunshot wound', 'Right eye injury', 'Right leg amputation',
    'Right lung puncture', 'Severe burns', 'Spinal cord injury',
    'Traumatic brain injury'
]

MALE_FIRST_NAMES = [
    'Andrew', 'Anthony', 'Brian', 'Charles', 'Christopher', 'Daniel', 'David',
    'James', 'John', 'Joseph', 'Kevin', 'Mark', 'Matthew', 'Michael', 'Paul',
    'Richard', 'Robert', 'Steven', 'Thomas', 'William'
]


LAST_NAMES = [
    'Anderson', 'Brown', 'Clark', 'Davis', 'Garcia', 'Harris', 'Jackson',
    'Johnson', 'Jones', 'Martin', 'Martinez', 'Miller', 'Moore', 'Smith',
    'Taylor', 'Thomas', 'Thompson', 'White', 'Williams', 'Wilson'
]

LOCATIONS = [
    'Beach', 'City', 'Countryside', 'Desert', 'Forest', 'Island', 'Jungle',
    'Mountain', 'Ocean', 'Tundra'
]

MEDICAL_SUPPLIES = [
    ('Chest Seal', 'Used to treat open chest wounds and prevent lung collapse'),
    ('Gauze', 'Used for wound dressing and absorbing blood'),
    ('Nasopharyngeal Airway', 'Used to maintain an open airway in unconscious patients'),
    ('Oxygen Mask', 'Used to deliver supplemental oxygen to patients with breathing difficulties'),
    ('Splint', 'Used to immobilize and support fractured bones or injured limbs'),
    ('Tourniquet', 'Used to control severe bleeding by constricting blood flow')
]

MENTAL_STATUS = ['calm', 'confused', 'upset', 'agony', 'unresponsive']

SEX = ['male', 'female']

TRIAGE_CATEGORIES = [
    ("minimal", "green", "Patients with minor injuries or stable conditions."),
    ("delayed", "yellow", "Patients with injuries requiring medical attention but not immediately life-threatening."),
    ("immediate", "red", "Patients with severe injuries requiring immediate medical attention."),
    ("expectant", "grey", "Patients with injuries or medical conditions where survival is unlikely."),
    ("deceased", "black", "Deceased patients.")
]

WEATHER_TYPES = [
    'Cloudy', 'Foggy', 'Hazy', 'Partly Cloudy', 'Rainy', 'Snowy', 'Stormy',
    'Sunny', 'Thunderstorm', 'Windy'
]

class ITMScenarioGenerator:
    def __init__(self):
        self.scenario_id = None

    def generate_random_id(self):
        return str(uuid.uuid4())

    def generate_scenario(self, total_patients=2):
        self.scenario_id = "scenario_" + self.generate_random_id()
        return Scenario(
            id=self.scenario_id,
            name="Triage Scenario 1",
            description=random.choice(DESCRIPTIONS),
            start_time=0,
            environment=None,
            patients=[self._generate_patient() for _ in range(total_patients)],
            medical_supplies=self._generate_medical_supplies(),
            triage_categories=self._generate_triage_categories()
        )

    def _generate_patient(self):
        sex = random.choice(SEX)
        first_name = random.choice(MALE_FIRST_NAMES) if sex == 'male' else \
                     random.choice(FEMALE_FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        age = random.randint(18, 80)
        num_injuries = random.randint(1, 5)
        injuries = random.sample(INJURIES, num_injuries)
        vitals = self._generate_vitals()
        patient_id = "patient_" + self.generate_random_id()
        name = f"{first_name} {last_name}"
        mental_status = random.choice(MENTAL_STATUS)
        patient = Patient(
            id=patient_id,
            name=name,
            age=age,
            sex=sex,
            injuries=injuries,
            vitals=vitals,
            mental_status=mental_status,
            assessed=False,
            tag='none'
        )
        return patient

    def _generate_vitals(self):
        heart_rate = random.randint(0, 160)
        systolic_pressure = str(random.randint(90, 140))
        diastolic_pressure = str(random.randint(60, 90))
        blood_pressure = f'{systolic_pressure} / {diastolic_pressure}'
        respiratory_rate = random.randint(0, 30)
        oxygen_level = random.randint(1, 100)
        vitals = Vitals(
            heart_rate=heart_rate,
            blood_pressure=blood_pressure,
            respiratory_rate=respiratory_rate,
            oxygen_level=oxygen_level
        )
        return vitals

    def _generate_medical_supplies(self):
        number_of_supplies = random.randint(1, len(MEDICAL_SUPPLIES))
        medical_supplies = random.sample(MEDICAL_SUPPLIES, number_of_supplies)
        inventory = [
            MedicalSupply(name=supply[0], description=supply[1], quantity=random.randint(1, 10))
            for supply in medical_supplies
        ]
        return inventory
    
    def generate_environment(self):
        weather = random.choice(WEATHER_TYPES)
        location = random.choice(LOCATIONS)
        visibility = 0.5
        noise_ambient = 0.5
        noise_peak = 0.5
        threat_level = 0.5
        environment = Environment(
            weather=weather,
            location=location,
            visibility=visibility,
            noise_ambient=noise_ambient,
            noise_peak=noise_peak,
            threat_level=threat_level
        )
        return environment

    def _generate_triage_categories(self):
        return [
            TriageCategory(color_tag=tc[0], description=tc[1], criteria=tc[2])
            for tc in TRIAGE_CATEGORIES
        ]

