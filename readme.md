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

-clone project from Github and cd into it
-
$ git clone <project>


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

-In bigger projects the task of running the application is moved
to a separate manage.py file in which case:

-run the appication locally
-
(venv)$ python manage.py

# Serving using production servers

-run the application locally using gunicorn
-

-run the application on Heroku using gunicorn
-




