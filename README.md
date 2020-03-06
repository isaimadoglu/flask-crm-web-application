# flask-crm-web-application
I'm developing a Flask-based web application.

Software Requirements:
- Python 3.7
- Flask 1.1.1
- SQLAlchemy
- pip
- virtualenv*

* Required Python modules are listed in "requirements.txt".

# Development Process

For Ubuntu 18.04:

- venv37 was created as a Python 3.7 virtual environment.
$ sudo apt install python3.7-venv
$ cd ./flask-crm-web-application
$ python3.7 -m venv venv37

- venv37 was sourced.
$ source venv37/bin/activate

- Flask module was installed.
$ pip install Flask    # Flask 1.1.1 is installed by default in python 3.7

- SQLAlchemy module was installed.
$ pip install flask_sqlalchemy

- Project folder was created.
$ mkdir crm && cd crm

- A database must be created to connect with flask application. sqlite3 is used
in this project. sqlite3 was installed and sqlite3 database was created.
$ sqlite3 crm_database
sqlite> .tables
sqlite> .exit

- "application.py" was created as main python file.
$ touch application.py
