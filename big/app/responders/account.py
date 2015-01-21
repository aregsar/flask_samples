from flask import Blueprint, render_template,url_for
from app import app

account = Blueprint('account', __name__)

@account.route("/signup")
def signup():
    return render_template("account/signup.html",page="account signup")


@account.route("/signin")
def signin():
    return render_template("account/signin.html",page="account signin")


@account.route("/account/details")
def details():
    return render_template("account/details.html",page="account details")
