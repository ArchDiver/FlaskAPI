from faker import faker

def getProfile():
    fake = Faker()
    return faker.profile()

from flask_api.models import Patient
from flask_api import db
import os
def seedData():
    form seed_num in range(10):
    data = getProfile()
    print(os.environ.get('DATABASE_URL'))
    print(data['name'], data['blood_group'])
    patient = Patient(
        data['name'],\
        data['sex'],\
        data['address'],\
        data['ssn'],\
        data['mail'])
    db.session.add(patient)
    db.session.commit()
seedData()

