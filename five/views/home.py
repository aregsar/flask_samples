from flask import Blueprint, render_template,url_for
from appp import app

home = Blueprint('home', __name__)

@home.route("/")
def index():
    print app.config['DEBUG']
    print app.config['DATABASE_URL']
    print app.config['SECRET_KEY']
    print url_for('home.index')
    print url_for('account.index')
    print url_for('account.details')
    return render_template("home/index.html",page="home.index")
