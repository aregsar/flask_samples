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
$ mkdir one

-move to project directory
-
$ cd one

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
$ git clone [projectname]


-move to project directory
-
$ cd one

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

# Serving using production servers

-run the application locally using gunicorn
-

-run the application on Heroku using gunicorn
-


# Flask resources

http://flask.pocoo.org/

https://exploreflask.com/

https://realpython.com/blog/

https://www.youtube.com/playlist?list=PLLjmbh6XPGK5e0IbpMccp7NmJHnN8O1ng

http://www.fullstackpython.com/flask.html

http://flaskbook.com/

http://blog.miguelgrinberg.com/

http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/#.VKxL7mTZln4

http://maximebf.com/blog/2012/11/getting-bigger-with-flask/#.VKxL0WTZln4

http://www.pluralsight.com/courses/flask-micro-framework-introduction

http://flask.pocoo.org/extensions/

# Common Flask extensions

http://flask-script.readthedocs.org/en/latest/

https://flask-wtf.readthedocs.org/en/latest/

https://pythonhosted.org/Flask-SQLAlchemy/

https://flask-migrate.readthedocs.org/en/latest/

https://flask-login.readthedocs.org/en/latest/

https://pythonhosted.org/Flask-Testing/





