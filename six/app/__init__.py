from flask import Flask
app = Flask(__name__)

from app.configs.settings import Settings
app.config.from_object(Settings)


print app.secret_key
print app.config['SECRET_KEY']
print app.debug
print app.config['DEBUG']

from app.views.home import home
app.register_blueprint(home)

from app.views.account import account
app.register_blueprint(account)

# from app.views import home
# app.register_blueprint(home.home)

# from app.views import account
# app.register_blueprint(account.account)

# from app.views import home
# app.register_blueprint(home.res)

# from app.views import account
# app.register_blueprint(account.res)


print app.url_map
