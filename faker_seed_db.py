from faker import Faker

def getProfile():
    fake = Faker()
    return fake.profile()

import os
from flask_api.models import Patient
from flask_api import db

def seedData():
    for seed_num in range(10):
        data = getProfile()
        print(os.environ.get('DATABASE_URL'))
        print(data['name'],data['blood_group'])
        patient = Patient(
            data['name'],\
            data['sex'],\
            data['address'],\
            data['ssn'],\
            data['blood_group'],\
            data['mail'])

        db.session.add(patient)
        db.session.commit()        
seedData()