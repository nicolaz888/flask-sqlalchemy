from config import db
from models.base_model import BaseModel


class Cohort(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    date_start = db.Column(db.Date, nullable=False)
