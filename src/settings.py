from flask import Flask
from flask_cors import CORS


class Settings:
    DEBUG = True  # para desarrollo
    ENV = "development"
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


application = Flask(__name__)
CORS(application)
application.config.from_object(Settings)
