from flask import Flask, redirect, url_for, abort

app = Flask(__name__)

@app.route("/")
def home():
    print url_for('home') # /
    print redirect(url_for('home')) # <Response 209 bytes [302 FOUND]>
    print url_for('hello') # /hello
    return redirect(url_for('hello')) # <Response 219 bytes [302 FOUND]>
    #return "Hello World"


@app.route("/hello")
def hello():
    return "hello"
    #return redirect(url_for('home'))

@app.route("/about")
def about():
    return "About", 200

@app.route("/abort")
def notfound():
    abort(404)

@app.route("/error")
def servererror():
    abort(500)


print app.url_map

if __name__ == "__main__":
    app.run(debug=True)
