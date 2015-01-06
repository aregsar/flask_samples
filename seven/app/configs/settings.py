import os

#secret key generation from python shell
#>>> import os
#>>> os.urandom(24)

#exported generated secret key in bash
#$ export SECRET_KEY='\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'


class Settings:
    ENV = os.environ.get('ENV')
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = bool(os.environ.get('DEBUG'))




