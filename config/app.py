from flask import Flask,url_for,redirect,render_template,abort,jsonify,request
app = Flask(__name__)

#------------------------------------------------------------------

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DATABASE_URL'] = "postgresql://username:password@localhost/dbname"

#-------------------------------------------------------------------

#app.config.from_object('settings')

#-------------------------------------------------------------------


# from config.settings import Settings
# app.config.from_object(Settings)


#----------------------------------------------------------------------


@app.route("/")
def index():
    return "Welcome home"


@app.route("/home")
def home():
    return str(app.debug)
    #return app.secret_key
    #return app.config['SECRET_KEY']
    #return app.config['DATABASE_URL']


print app.url_map

if __name__ == "__main__":
    app.run(debug=True)
    #app.run()
