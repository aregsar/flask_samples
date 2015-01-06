
"""
the most simple
flask application
"""

#the most simple
#flask application

from flask import Flask
app = Flask(__name__)

#@app.route("/home")
@app.route("/")
def hello():
    return "Hello World"


#print app.url_map

#run the application from command line
if __name__ == "__main__":
    app.run(debug=True)
