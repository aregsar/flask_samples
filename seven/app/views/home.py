from flask import Blueprint, render_template,url_for
from app import app

#res = Blueprint('home', __name__)
home = Blueprint('home', __name__)

#@res.route("/")
@home.route("/")
def index():
    print app.config['DEBUG']
    print app.config['DATABASE_URL']
    print url_for('home.index')
    print url_for('account.index')
    print url_for('account.details')
    return render_template("home/index.html",page="home.index")
