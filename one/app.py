from flask import Flask,url_for,redirect
app = Flask(__name__)

# from app.configs.settings import Settings
# app.config.from_object(Settings)

# print app.secret_key
# print app.config['SECRET_KEY']
# print app.debug
# print app.config['DEBUG']


# @app.route("/")
# def home():
#     return "Welcome home"


# @app.route("/")
# def home():
#     return url_for("home")


#@app.route('/user/<int:id>/<username>', strict_slashes=False
# @app.route("/home")
# @app.route("/")
# def home():
#     return url_for("home")


# @app.route("/home", defaults={"name":"bob"})
# @app.route("/home/<name>")
# def home(name):
#     print name
#     return name
#     #return url_for("home",name=name)

# @app.route('/user/<int:id>')
# def home(id):
#     return url_for("home",id=id)



# @app.route("/home")
# def gohome():
#     return redirect(url_for('home'))

# @app.route("/about")
# def about():
#     return "About", 200

# @app.route("/abort")
# def notfound():
#     abort(404)

# @app.route("/error")
# def servererror():
#     abort(500)


# @app.route("/about")
# def about():
#     return jsonify(name="flask",age=5)


# @app.route("/about")
# def about():
#     return jsonify({"name":"flask","age":5})

# @app.route('/home', methods=["GET","POST"])
# #@app.route('/home', methods=["GET"])
# #@app.route('/home', methods=["POST"])
# def again():
#     return url_for("again")


# @app.route('/create', methods=["GET","POST"])
# def create():
#     if request.method == 'POST':
#         return "POST"
#     return "GET"

# @app.route("/index")
# def index():
#     return render_template("index.html")

# @app.route('/index')
# def index():
#     return render_template('index.html',var='abcd')


# @app.errorhandler(404)
# def page_not_found(error):
#     return 'The page you requested does not exist', 404


# @app.errorhandler(500)
# def internal_server_error_handler(error):
#     return render_template("500.html"), 500

# @app.errorhandler(Exception)
# def exception_handler(error):
#     if request.is_xhr:
#         return jsonify(status="error",message="there was an error"), 500
#     return repr(error), 500

print app.url_map

if __name__ == "__main__":
    app.run(debug=True)
