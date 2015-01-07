from flask import Flask
app = Flask(__name__)

app.config['DATABASE_URL'] = "postgres"
app.config['DEBUG'] = True

app.config.from_object('settings')


from views.home import home
app.register_blueprint(home)

from views.account import account
app.register_blueprint(account)


print app.url_map




