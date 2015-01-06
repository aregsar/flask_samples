from flask import Flask, render_template, redirect, url_for, abort, jsonify,request

app = Flask(__name__)

class PostgresConnectionError(Exception):
    pass

@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/dberror")
def dberror():
    raise PostgresConnectionError

@app.errorhandler(PostgresConnectionError)
def postgres_exception_handler(error):
    return repr(error), 500
    #return render_template("500.html"), 500

@app.route("/generror")
def generror():
    raise Exception("postgress connection error")

@app.errorhandler(Exception)
def exception_handler(error):
    if request.is_xhr:
        return jsonify(status="error",message="there was an error"), 500
    return repr(error), 500

print app.url_map

if __name__ == "__main__":
    app.run(debug=True)

