import os

class Settings:
    DEBUG = bool(os.environ.get('DEBUG'))
    SECRET_KEY = os.environ['SECRET_KEY']
    DATABASE_URL = os.environ.get('DATABASE_URL')



