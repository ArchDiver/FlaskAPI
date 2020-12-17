

#   #route for creating Patients
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

#   #route for Retreiving ALL Patients data
@app.route('/patients', methods = ['GET'])
def get_patients():
    patients = Patients.query.all()
    return jsonify(patients_schema.dumps(patients))


"""
route for retieving a SINGLE patient's data
expects = ID
"""
@app.route(('/patients/<id>', methods = ['GET']))
def get_patients():
    patient = Patient.query.get(id)
    results = patient_schema.dumps(patient)
    return jsonify(results)


"""
route for UPDATING patient data based on ID
expects = ID
"""
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

"""
route for deleting a SINGLE patient data
expects = ID
"""
@app.route('/patients/delete/<id>', methods = ['DELETE'])
def delete_patients(id):
    patient = Patient.query.get(int(id))
    db.session.delete(patient)
    db.session.commit()
    result = patient_schema.dumps(patient)
    return jsonify(result)

@app.route('/')
def home():
    return render_template('home.html')


#   # route to the REGISTER page
@route('/users/register', methods = ['GET', 'POST'])
def register():
    from = UserForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        user = User(name, email, password)

        db.session.add(user)
        db.session.commit(user)

        return redirect(url_for('login'))
    return render_template('request.html', form = form)

#   # route to the LOGIN page
@app.route('/users/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data

    logged_user = user.query.filter(User.email == email).first()
    if logged_user and check_password_hash(logged_user.password, password):
        login_user(logged_user)
        return redirect(url_for('get_key'))
    return render_template('login.html', form = form)