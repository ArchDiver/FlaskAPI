from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_marshmellow import Marshmellow

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

