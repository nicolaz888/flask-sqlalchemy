from config import db
from models.base_model import BaseModel


class Campus(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    short_name = db.Column(db.String(5), unique=True, nullable=False)
