from flask import Blueprint, render_template,url_for
from app import app

#res = Blueprint('account', __name__)
account = Blueprint('account', __name__)

#@res.route("/account")
@account.route("/account")
def index():
    print app.config['DEBUG']
    print app.config['DATABASE_URL']
    print url_for('account.index')
    print url_for('account.details')
    print url_for('home.index')
    return render_template("account/index.html",page="account.index")



#@res.route("/account/details")
@account.route("/account/details")
def details():
    print app.config['DEBUG']
    print app.config['DATABASE_URL']
    print url_for('account.index')
    print url_for('account.details')
    print url_for('home.index')
    return render_template("account/details.html",page="account.details")
