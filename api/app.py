from flask import Flask,url_for,redirect,render_template,abort,jsonify,request
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome home"

@app.route("/items")
def items():
    return "items"


print ""
print app.url_map
print ""

if __name__ == "__main__":
    app.run(debug=True)
