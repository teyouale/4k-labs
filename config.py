import os


class Config:
    MAX_CONTENT_LENGTH = 30 * 1024 * 1024
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'anything but string'
    MONOGO_URI = 'mongodb://localhost:27017/4kdevelopment'
    CV_PATH = './cv'
    ALLOWED_EXTENSIONS = {'pdf','docs','doc','rtf'}
class development_config(Config):
    DEBUG=True

class production_config(Config):
     MONOGO_URI = 'mongodb://localhost:27017/4kproduction'

configuration = {
    'development':development_config,
    'production':production_config,
    'default':development_config
}