from flask import Flask,redirect,url_for,render_template,request
from flask_pymongo import PyMongo
from flask_cors import CORS
from config import Config,configuration
from flask_jwt_extended import create_access_token,get_jwt
import os


#  Add Cors and pyjwt

mongo = PyMongo()
db = mongo.db

app = Flask(__name__)


def create_app(config_name):
    app.config.from_object(configuration[config_name])
    mongo.init_app(app,uri=configuration[config_name].MONOGO_URI)
    cors = CORS(app, resources={r"/api_v1/*": {"origins": "*"}},supports_credentials=True)
    from .api_v1 import api_v1
    app.register_blueprint(api_v1)
    return app