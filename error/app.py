from flask import Flask,url_for,redirect,render_template,abort,jsonify,request
app = Flask(__name__)

#----------------------------------------------------------------------


@app.route("/")
def index():
    return "Welcome home"

#-------------------------------------------------------------------------

@app.route("/abort")
def notfound():
    abort(500)

# @app.errorhandler(500)
# def page_not_found(error):
#     return error, 404

#-------------------------------------------------------------------------

@app.route("/error")
def error():
    raise Exception("error")

# @app.errorhandler(Exception)
# def exception_handler(error):
#     return render_template("500.html"), 500


# @app.errorhandler(Exception)
# def exception_handler(error):
#     if request.is_xhr:
#         return "<h1>Server Error</h1>", 500
#     return jsonify(status="error",message="there was an error"), 500


#-------------------------------------------------------------------------

class PostgresConnectionError(Exception):
    pass

@app.route("/errordb")
def dberror():
    raise PostgresConnectionError

@app.errorhandler(PostgresConnectionError)
def postgres_exception_handler(error):
    return repr(error), 500

#--------------------------------------------------------------------------

print app.url_map

if __name__ == "__main__":
    app.run(debug=True)
