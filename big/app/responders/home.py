from flask import Blueprint, render_template,url_for
from app import app

home = Blueprint('home', __name__)

@home.route("/")
def index():
    return render_template("home/index.html",page="home")

@home.route("/about")
def about():
    return render_template("home/about.html",page="about")

@home.route("/company")
def contact():
    return render_template("home/info.html",page="contact")
