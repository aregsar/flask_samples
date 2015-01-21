from flask import Flask,url_for,redirect,render_template,abort,jsonify,request
app = Flask(__name__)

#----------------------------------------------------------------------


@app.route("/")
def index():
    return "Welcome home"

#-------------------------------------------------------------------------

# @app.route("/abort")
# def notfound():
#     abort(404)

#-------------------------------------------------------------------------

# @app.route('/index')
# def index():
#     abort(404)

# @app.errorhandler(404)
# def page_not_found(error):
#     return '404 error', 404
#-------------------------------------------------------------------------

# @app.route("/error")
# def error():
#     raise Exception("error")

# @app.errorhandler(Exception)
# def exception_handler(error):
#     return render_template("500.html"), 500

#-------------------------------------------------------------------------

# @app.
# route("/error")
# def error():
#     raise Exception("error")

# @app.errorhandler(Exception)
# def exception_handler(error):
#     if request.is_xhr:
#         return jsonify(status="error",message="there was an error"), 500
#     return render_template("500.html"), 500

#-------------------------------------------------------------------------


print app.url_map

if __name__ == "__main__":
    app.run(debug=True)
