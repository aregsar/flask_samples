from flask import Flask, render_template, redirect, url_for, abort, jsonify,request

app = Flask(__name__)


@app.route("/")
def home():
    #print(jsonify(request.script_root))
    return render_template("hello.html")

@app.route("/about")
def about():
    return jsonify(name="areg",age=50)
    #return jsonify({"name":"areg","age":50})

@app.route("/error")
def servererror():
    abort(500)

@app.errorhandler(404)
def page_not_found(error):
    return 'The page you requested does not exist', 404

@app.errorhandler(500)
def internal_server_error_handler(error):
    return render_template("500.html"), 500

class PostgresConnectionError(Exception):
    pass

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
    return repr(error), 500

print app.url_map

if __name__ == "__main__":
    app.run(debug=True)

