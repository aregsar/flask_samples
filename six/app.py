from flask import Flask
app = Flask(__name__)

from views.home import home
app.register_blueprint(home)

from views.account import account
app.register_blueprint(account)

app.config['DATABASE_URL'] = "postgres"

print app.url_map


