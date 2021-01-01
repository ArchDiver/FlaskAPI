from flask_api import app, db
from flask_api.models import Patient, patient_schema, patients_schema, User, check_password_hash
from flask import jsonify, request, render_template, redirect, url_for, flash, session, Blueprint

# Import for Flask Login
from flask_login import login_required, login_user, current_user,logout_user

# Import for PyJWT (Json Web Token)
import jwt

from flask_api.forms import UserForm, LoginForm
from .token_validation import token_required

bp = Blueprint('routes', __name__)

@app.route('/')
def home():
    return render_template('home.html')


##################################################
##################  Patient Records ##############
##################################################

#   #route for creating Patients
@app.route('/patients/create', methods = ['POST'])
@token_required
def create_patient(current_user_token):
    firstName = request.json['first_name']
    lastName = request.json['last_name']
    gender = request.json['gender']
    address = request.json['address']
    ssn = request.json['ssn']
    blood_type = request.json['blood_type']
    email = request.json['email']

    patient = Patient(firstName, lastName, gender, address, ssn, blood_type, email)
    results = patient_schema.dump(patient)
    flash(f"Record for {patient} has been added.", "info")
    return jsonify(results)

#   #route for Retreiving ALL Patients data
@app.route('/patients', methods = ['GET'])
@token_required
def get_patients(current_user_token):
    patients = Patient.query.all(current_user_token)
    return jsonify(patients_schema.dumps(patients))


"""
route for retieving a SINGLE patient's data
expects = ID
"""
@app.route('/patients/<id>', methods = ['GET'])
@token_required
def get_patient(current_user_token, id):
    patient = Patient.query.get(current_user_token, id)
    results = patient_schema.dumps(patient)
    return jsonify(results)


"""
route for UPDATING patient data based on ID
expects = ID
"""
@app.route('/patients.<id>', methods = ['POST', 'PUT'])
@token_required
def update_patients(current_user_token, id):
    patient = Patient.query.get(current_user_token, id)
    patient.name = request.json['full_name']
    patient.gender = request.json['gender']
    patient.address = request.json['address']
    patient.ssn = request.json['ssn']
    patient.blood_type = request.json['blood_type']
    patient.email = request.json['email']

    db.session.commit()

    return patient_schema.jsonify(patient)

"""
route for deleting a SINGLE patient data
expects = ID
"""
@app.route('/patients/delete/<id>', methods = ['DELETE'])
@token_required
def delete_patients(current_user_token, id):
    patient = Patient.query.get(int(id))
    db.session.delete(patient)
    db.session.commit()
    result = patient_schema.dumps(patient)
    return jsonify(result)



##################################################
################### Users ########################
##################################################

#   # route to the REGISTER page
@app.route('/users/register', methods = ['GET', 'POST'])
def register():
    form = UserForm()
    if request.method == 'POST' and form.validate():
        fullName = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(fullName, email, password)
        db.session.add(user)
        db.session.commit(user)
        flash("You have been registered. You will use your email and password to login.", "info")

        return redirect(url_for('home'))
    return render_template('register.html', form = form)

#   # route to the LOGIN page
@app.route('/users/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    logged_user = User.query.filter(User.email == email).first()
    if logged_user and check_password_hash(logged_user.password, password):
        login_user(logged_user)
        flash(f"You are now logged in as {logged_user}.")
        return redirect(url_for('get_key'))
    flash(f"Not a valid user or password. Please try again or register")
    return render_template('login.html', form = form)

@app.route('/users/logout')
def logout():
    if "user" in session:
        session.pop("user", None)
        flash("You have been logged out.", "info")

@app.route('/getkey', methods = ['GET'])
def get_key():
    token = jwt.encode({'public_id':current_user.id, 'email':current_user.email}, app.config['SECRET_KEY'])
    user = User.query.filter_by(email = current_user.email).first(token)
    user.token = token

    db.session.add(user)
    db.session.commit()
    results = token.decode('utf-8')
    return render_template('token.html', results = results)

@app.route('/updatekey', methods = ['GET','POST','PUT'])
def refresh_key():
    refresh_key = {'refreshToken': jwt.encode({'public_id':current_user.id, 'email':current_user.email}, app.config['SECRET_KEY'])}
    temp = refresh_key.get('refreshToken')
    actual_token = temp.decode('utf-8')
    return render_template('token_refresh.html', actual_token = actual_token)