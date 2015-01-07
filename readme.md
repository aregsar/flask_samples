# Python development environment Setup (OSX only)

-install homebrew
-
$ ruby -e "$(curl -fsSL https-//raw.github.com/Homebrew/homebrew/go/install)"

-install python 2.7 and pip 2.7 with homebrew
-
$ brew install python

-install virtualenv with pip
-
$ pip install virtualenv


# New Flask project setup (OSX and Linux)

-create the project directory
-
$ mkdir [projectname]

-move to project directory
-
$ cd [projectname]

-create virtual environment and venv subfolder - one time per project operation
-
$ virtualenv -p $(which python) venv

-activate (or re-activate) the virtual environment
-
$ . venv/bin/activate

-install the flask package - specifying the version is optional
-
(venv)$ pip install Flask==0.10.1

-create (or re-create) requirements.txt with installed packages.
-
(venv)$ pip freeze > requirements.txt

-create application
-
(venv)$ touch app.py

-run the appication
-
(venv)$ python app.py

-de-activate the virtual environment
-
(venv)$ deactivate



# Cloned Flask Project Setup (OSX and Linux)

-clone project from Github
-
$ git clone [projectURL]


-move to project directory
-
$ cd [projectname]

-create virtual environment and venv subfolder - one time per project operation
-
$ virtualenv -p $(which python) venv

-activate (or re-activate) the virtual environment
-
$ . venv/bin/activate

-install (or re-install) python packages listed in requirements.txt file
-
(venv)$ pip install -r requirements.txt

-run the appication
-
(venv)$ python app.py

-deactivate the virtual environment
-
(venv)$ deactivate

# Running the application using manage.py

-In some projects the code for running the application is moved
to a separate manage.py file in the root directory of the project

-run the application
-
(venv)$ python manage.py

# Using autoenv to automatically activate the virtual environment
and export environment variables

-install autoenv with pip
-
$ pip install autoenv

-configure autoenv
-
$ echo 'source /usr/local/bin/activate.sh' >> ~/.bash_profile

-add a .env file to project root

-add ". venv/bin/activate" without the quotes to the .env file

-add "export DEBUG=True" without the quotes to the .env file

-Now whenever you cd into the project directory the .env file is executed
automatically activating the virtual envoronment and exporting any exported variables


# Serving using production servers

-run the application locally using gunicorn
-

The general form of the command for running with gunicorn is:
-
gunicorn -b 127.0.0.1:4000 [flask application instance container]:[flask application instance name]

-
where [flask application instance container] is a file or directory inside the project root.
If it is a file then it is the name of the file in which the app instance is created or
the name of the file that imports the app instance. If it is a directory then it is
the name of a python package directory where the app instance resides inside the [__init__.py] file

Example where the flask application instance named app
is imported in a manage.py file.

(venv)$ gunicorn -b 127.0.0.1:4000 manage:app

Example where the flask application instance named app
is created inside the app.py file
or is created in the __init__.py file inside a directory named app.

(venv)$ gunicorn -b 127.0.0.1:4000 app:app


-run the application on Heroku using gunicorn
-

in Procfile add:

web: gunicorn manage:app

or

web: gunicorn app:app

# Flask resources

the flask website
http://flask.pocoo.org/

an online reference book that also coveres organising large flask apps with blueprints
https://exploreflask.com/

the best step by step online tutorials for flask
https://realpython.com/blog/

the realpython youtube channel:
https://www.youtube.com/playlist?list=PLLjmbh6XPGK5e0IbpMccp7NmJHnN8O1ng

a compilation of flask resources
http://www.fullstackpython.com/flask.html

The definitive flask book from oreilly
http://flaskbook.com/

exellent blog from the author of the orielly flask book
http://blog.miguelgrinberg.com/

this sets up a basic flask app including self hosting server configuration
http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/#.VKxL7mTZln4

this covers the use of blueprints
http://maximebf.com/blog/2012/11/getting-bigger-with-flask/#.VKxL0WTZln4

excellent intro to flask. Requires a subscription but has free trial period.
http://www.pluralsight.com/courses/flask-micro-framework-introduction

flask approved extension list
http://flask.pocoo.org/extensions/

# Common Flask extensions

for running tasks from command line:
http://flask-script.readthedocs.org/en/latest/

for html form handling and validation:
https://flask-wtf.readthedocs.org/en/latest/

for data models and ORM:
https://pythonhosted.org/Flask-SQLAlchemy/

for database schema migrations:
https://flask-migrate.readthedocs.org/en/latest/

for user authentication:
https://flask-login.readthedocs.org/en/latest/

for testing:
https://pythonhosted.org/Flask-Testing/





