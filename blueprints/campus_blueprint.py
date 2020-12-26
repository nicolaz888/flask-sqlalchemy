from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt import jwt_required

from config import db
from models.campus import Campus
from models.user import User

campus_blueprint = Blueprint('campus_blueprint', __name__)


@campus_blueprint.route('/campuses')
@swag_from('../flasgger/get_campuses.yml')
@jwt_required()
def get_campuses():
    try:
        campuses = Campus.query.all()
        return {'campuses': [campus.to_json() for campus in campuses]}, 200
    except Exception as e:
        print(f'error en get_campuses(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500


@campus_blueprint.route('/campus', methods=['POST'])
@swag_from('../flasgger/create_campus.yml')
@jwt_required()
def create_campus():
    try:
        body_json: dict = request.json

        name_body: str = body_json['name']
        short_name_body: str = body_json['short_name']

        new_campus: Campus = Campus(name=name_body, short_name=short_name_body)
        db.session.add(new_campus)
        db.session.commit()

        return {'message': 'hola putos'}, 202

    except Exception as e:
        print(f'error en create_event(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500
