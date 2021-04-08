import os
from datetime import timedelta


class Config:
    CORS_HEADERS = ['Content-Type','Authorization']
    MAX_CONTENT_LENGTH = 30 * 1024 * 1024
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'anything but string'
    MONOGO_URI = 'mongodb://localhost:27017/4kdevelopment'
    CV_PATH = './cv'
    PROFILE_PICTURES = './profile'
    THUMBNAILS = './thumbnails'
    ALLOWED_EXTENSIONS = {'pdf','docs','doc','rtf'}
    # jwt configuration
    JWT_TOKEN_LOCATION = "headers"
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or 'anything but string'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
class development_config(Config):
    DEBUG=True

class production_config(Config):
     MONOGO_URI = 'mongodb://localhost:27017/4kproduction'

configuration = {
    'development':development_config,
    'production':production_config,
    'default':development_config
}