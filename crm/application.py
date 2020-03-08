from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os # to give path of sqlite3 database

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "crm/crm_database")
ORM_DIR = 'sqlite:////' + DB_DIR    # to use db in sqlalchemy orm structure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ORM_DIR
db = SQLAlchemy(app)

@app.route("/")
def index():
  leads = Lead.query.all()
  return render_template("index.html", leads = leads)

@app.route("/lead-add")
def lead_add_page():
    return render_template("lead-add.html")
@app.route("/lead-add-function", methods = ["POST"])
def lead_add():
    name = request.form.get("name")
    company = request.form.get("company")
    phone = request.form.get("phone")
    email = request.form.get("email")
    new_lead = Lead(name = name, company = company, phone = phone, email = email)
    db.session.add(new_lead)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/touch-data")
def touch_data():
  touches = Touch.query.all()
  return render_template("touch-data.html")

@app.route("/touch-add")
def touch_add_page():
    touches = Touch.query.all()
    leads = Lead.query.all()

    return render_template("touch-add.html", leads = leads, touches = touches)
@app.route("/touch-add-function", methods = ["POST"])
def touch_add():
    lead_id = request.form.get("lead_id")
    date = request.form.get("date")
    description = request.form.get("description")
    new_touch = Touch(lead_id = lead_id, date = date, description = description)
    db.session.add(new_touch)
    db.session.commit()
    return redirect(url_for("touch_data"))

# classes for database will be created.
class Lead(db.Model):
  """
  Information of soon-to-be-customers are holded here.
  """
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40))
  company = db.Column(db.String(80))
  phone = db.Column(db.String(20))
  email = db.Column(db.String(40))
  touches = db.relationship('Touch', backref='lead', lazy=True)

  def __init__(self, name, company, phone, email):
      self.name = name
      self.company = company
      self.phone = phone
      self.email = email

  def __repr__(self):
      return '<Lead %r>' % self.name

class Touch(db.Model):
  """
  Data of all the times of calling or mailing leads.
  """
  id = db.Column(db.Integer, primary_key=True)
  lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
  date = db.Column(db.DateTime)
  description = db.Column(db.String(200))

  def __init__(self, lead_id, date, description):
      self.lead_id = lead_id
      self.date = date
      self.description = description

  def __repr__(self):
      return '<Touch %r>' % self.description

if __name__ == "__main__":
  db.create_all()
  app.run(debug=True)
