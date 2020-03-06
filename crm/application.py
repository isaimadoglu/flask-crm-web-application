from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

import os # to give path of sqlite3 database

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "crm/crm_database")
ORM_DIR = 'sqlite:////' + DB_DIR    # to use db in sqlalchemy orm structure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ORM_DIR
db = SQLAlchemy(app)

@app.route("/")
def index():
  return render_template("index.html")

# classes for database will be created.
class Lead(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40))
  company = db.Column(db.String(80))
  phone = db.Column(db.String(20))
  email = db.Column(db.String(40))

class Touch(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  #lead = db.Column()
  #date = db.Column()
  description = db.Column(db.String(200))
  
if __name__ = "__main__":
  db.create_all()
  app.run(debug=True)
