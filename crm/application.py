from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os # to give path of sqlite3 database

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "crm/crm_database")
ORM_DIR = 'sqlite:////' + DB_DIR    # to use db in sqlalchemy orm structure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ORM_DIR
db = SQLAlchemy(app)

# classes for database will be created.
