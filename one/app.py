from flask import Flask,url_for,redirect,render_template,abort,jsonify,request
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome home"


#-------------------------------------------------------------------------


# @app.route("/home")
# def home():
#     return url_for("home")

#-------------------------------------------------------------------------


# @app.route("/home")
# def some():
#     return url_for("some")


#-------------------------------------------------------------------------

# @app.route("/home/<names>")
# def home(names):
#     return names


#-------------------------------------------------------------------------

# @app.route('/home/<int:id>')
# def user(id):
#     return url_for("user",id=id)

#-------------------------------------------------------------------------


# @app.route("/home", defaults={"name":"bob"})
# @app.route("/home/<name>")
# def home(name):
#     return name

#-------------------------------------------------------------------------

# @app.route("/home")
# def gotoindex():
#     return redirect(url_for('index'))

#-------------------------------------------------------------------------

# @app.route('/home', methods=["GET"])
# def home():
#     return "GET home"

#-------------------------------------------------------------------------

# @app.route('/home', methods=["GET","POST"])
# def create():
#     return "GET or POST home"

#-------------------------------------------------------------------------

# @app.route('/home', methods=["POST"])
# def create():
#     return "POST home"

#-------------------------------------------------------------------------

# @app.route('/home', methods=["GET","POST"])
# def create():
#     if request.method == 'GET':
#         return "GET home"
#     return "POST home"

#-------------------------------------------------------------------------

# @app.route("/home")
# def home():
#     return jsonify(name="flask",age=5)

#-------------------------------------------------------------------------

# @app.route("/home")
# def home():
#     return jsonify({"name":"flask","age":5})

#-------------------------------------------------------------------------

# @app.route("/home")
# def home():
#     return render_template("index.html")

#-------------------------------------------------------------------------

# @app.route('/home')
# def home():
#     return render_template('index.html',name='bob')

#-------------------------------------------------------------------------


print app.url_map

if __name__ == "__main__":
    app.run(debug=True)
