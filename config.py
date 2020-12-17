import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random_acts_of_kindness!!36'
    SQLACHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLACHEMY_TRACK_MODIFICATIONS = False # silence the depreation warning