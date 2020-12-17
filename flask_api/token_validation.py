from functools import wraps
from flask import request, jsonify

from flask_api import app

from flask_api.models import User

import jwt

# Custom Decorator to validate API KEY Token is passed to a specific route
def token_required(our_flask_function):
    @wraps(our_flask_function) # Copy the contents of the returned function, specifically the parameters
    def decorated(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}),401

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user_token = User.query.filter_by(id = data['public_id']).first()
            print(token)
            print(data)
        except:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            print(data)
            print(token)
            return jsonify({'message': 'Token is invalid'}), 401
        return our_flask_function(current_user_token, *args,**kwargs)

    return decorated