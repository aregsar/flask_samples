from flask import Blueprint, render_template,url_for
from app import app


account = Blueprint('account', __name__)


@account.route("/account")
def index():
    print app.config['DEBUG']
    print app.debug
    print app.config['SECRET_KEY']
    print url_for('account.index')
    print url_for('account.details')
    print url_for('home.index')
    return render_template("account/index.html",page="account.index")



@account.route("/account/details")
def details():
    print app.config['DEBUG']
    print app.debug
    print app.config['SECRET_KEY']
    print url_for('account.index')
    print url_for('account.details')
    print url_for('home.index')
    return render_template("account/details.html",page="account.details")
