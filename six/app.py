from flask import Flask
app = Flask(__name__)


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


app.config['DATABASE_URL'] = "postgres"

print app.url_map


