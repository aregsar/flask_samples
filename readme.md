
# OSX installation instructions


# Environment Setup

-install homebrew
$ ruby -e "$(curl -fsSL https-//raw.github.com/Homebrew/homebrew/go/install)"

-install python 2.7 and pip 2.7 with homebrew
$ brew install python

-install virtualenv with pip
$ pip install virtualenv


# New Project Setup

-create the project directory and cd into it
$ mkdir one
$ cd one

-create virtual environment and venv subfolder - one time operation
$ virtualenv -p $(which python) venv

-activate (or re-activate) the virtual environment
$ . venv/bin/activate

-install the flask package - specifying the version is optional
(venv)$ pip install Flask==0.10.1

-create (or re-create) requirements.txt with installed packages.
(venv)$ pip freeze > requirements.txt

-create application
(venv)$ touch app.py

-run the appication
(venv)$ python app.py

-de-activate the virtual environment
(venv)$ deactivate



# Clone from Github

-clone project from Github and cd into it
$ git clone git@github.com:aregsar/one.git
$ cd one

-create virtual environment and venv subfolder - one time operation
$ virtualenv -p $(which python) venv

-activate (or re-activate) the virtual environment
$ . venv/bin/activate

-install (or re-install) python packages listed in requirements.txt file
(venv)$ pip install -r requirements.txt

-run the appication
(venv)$ python app.py

-deactivate the virtual environment
(venv)$ deactivate

# Serving using manage.py

-run the appication locally
(venv)$ python manage.py

# Serving using production servers

-run the application locally using gunicorn

-run the application on Heroku using gunicorn




