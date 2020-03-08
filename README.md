# flask-crm-web-application
I'm developing a Flask-based web application.

Software Requirements:
- Python 3.7
- Flask 1.1.1
- SQLAlchemy
- pip
- virtualenv*

* Required Python modules are listed in "requirements.txt".

# How to Run the application

- First of all the project should be downloaded.
- venv37 can be deleted, because different computers may not run the same virtual environments.
- A new Python 3.7 version virtual environment can be created and required modules can be installed using the commend below:
$ pip install -r requirements.text
- Python virtual environment should be sourced using the command below:
$ source venv/bin/activate  # supposed that name of the virtualenv is "venv"
- Now "crm" directory is used anymore.
$ cd crm
- A new sqlite3 database must be created with the commands below:
$ sqlite3 crm_database
sqlite> .tables
sqlite> .exit
- It is ready to run.
$ python application.py
- The application can be used over a web browser.
Url-> localhost:5000

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
