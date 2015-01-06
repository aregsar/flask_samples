from flask import Flask, render_template, abort, jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/about")
def about():
    return jsonify(name="flask",age=5)
    #return jsonify({"name":"flask","age":5})

@app.route('/create', methods=["GET","POST"])
def create():
    if request.method == 'GET':
        return jsonify(name="flask",age=5)
    return render_template('name.html',name='create')

@app.route('/user/<int:id>')
def get(id):
    app.logger.debug('app.logger.debug - id == %d', id)
    app.logger.warning('app.logger.warning')
    app.logger.error('app.logger.error')
    return render_template('name.html',name='get')


@app.route('/user', defaults={'name': 'flask'})
@app.route('/user/<name>')
def show(name):
    return render_template('name.html',name=name)

@app.route("/abort")
def notfound():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return 'The page you requested does not exist', 404

@app.route("/error")
def servererror():
    abort(500)

@app.errorhandler(500)
def internal_server_error_handler(error):
    return render_template("500.html"), 500


print app.url_map

if __name__ == "__main__":
    app.run(debug=True)

