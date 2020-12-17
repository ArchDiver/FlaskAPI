@app.route('/paternts/create', methods = ['POST'])
def create_patient():
    name = request.json['full_name']
    gender = request.json['gender']
    address = request.json['address']
    ssn = request.json['ssn']
    blood_type = request.json['blood_type']
    email = request.json['email']

    patient = Patient(name, gender, address, ssn, blood_type, email)
    results = patient_schema.dump(patient)
    return jsonify(results)

@app.route('/patients', methods = ['GET'])
def get_patients():
    patients = Patients.query.all()
    return jsonify(patients_schema.dumps(patients))


@app.route(('/patients/<id>', methods = ['GET']))
def get_patients():
    patient = Patient.query.get(id)
    results = patient_schema.dumps(patient)
    return jsonify(results)

@app.route('/patients.<id>', methods = ['POST', 'PUT'])
def update_patients():
    pattient = Patient.query.get(id)

    patient.name = request.json['full_name']
    patient.gender = request.json['gender']
    patient.address = request.json['address']
    patient.ssn = request.json['ssn']
    patient.blood_type = request.json['blood_type']
    patient.email = request.json['email']

    db.session.commit()

    reutrn patient_schema.jsonify(patient)

@app.route('/patients/delete/<id>', methods = ['DELETE'])
def delete_patients(id):
    patient = Patient.query.get(int(id))
    db.session.delete(patient)
    db.session.commit()
    result = patient_schema.dumps(patient)
    return jsonify(result)