import datetime

from flasgger import Swagger
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/db2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(minutes=30)

Swagger(app)

db = SQLAlchemy(app)

event_cohort = db.Table('event_cohort',
                        db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                        db.Column('cohort_id', db.Integer, db.ForeignKey('cohort.id'), primary_key=True)
                        )

event_campus = db.Table('event_campus',
                        db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                        db.Column('campus_id', db.Integer, db.ForeignKey('campus.id'), primary_key=True)
                        )
