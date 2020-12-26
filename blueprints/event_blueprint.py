from datetime import date

from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt import jwt_required

from config import db, event_cohort
from daos.campus_dao import CampusDAO
from daos.cohort_dao import CohortDAO
from daos.event_dao import EventDAO
from models.cohort import Cohort
from models.event import Event
from models.user import User
from utils import date_util
from validators.Validator import Validator

event_blueprint = Blueprint('event_blueprint', __name__)


@event_blueprint.route('/events')
@swag_from('../flasgger/get_events.yml')
@jwt_required()
def get_events():
    try:
        events = Event.query.all()
        return {'events': [element.to_json() for element in events]}, 200
    except Exception as e:
        print(f'error en get_events(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500


@event_blueprint.route('/event/<event_id>', methods=['GET', 'PUT'])
@swag_from('../flasgger/event.yml')
@jwt_required()
def event(event_id: int):
    try:
        result: Event = Event.query.get(event_id)

        if request.method == 'GET':
            return {'event': result.to_json()}, 200

        elif request.method == 'PUT':

            body_json: dict = request.json

            name_body: str = body_json.get('name')

            if name_body:
                result.name = name_body

            db.session.commit()

            return {'message': 'hola PUTos'}, 200

    except Exception as e:
        print(f'error en get_events(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500


@event_blueprint.route('/event', methods=['POST'])
@swag_from('../flasgger/create_event.yml')
@jwt_required()
def create_event():
    try:
        body_json: dict = request.json

        name: str = body_json.get('name') or ''
        date_body: str = body_json.get('date') or ''
        user_id: int = int(body_json.get('user_id')) if body_json.get('user_id') else -1
        attendees: int = int(body_json.get('attendees')) if body_json.get('attendees') else -1
        type_body: int = int(body_json.get('type')) if body_json.get('type') else -1
        cohorts_body: list = body_json.get('cohorts') or []
        campuses_body: list = body_json.get('campuses') or []

        create: bool = Validator.validate(name, date_body, user_id, attendees, type_body, cohorts_body, campuses_body)

        if create:
            date_final = date_util.get_date(date_body)
            new_event: Event = Event(name=name, date=date_final, created_by=user_id, attendees=attendees,
                                     type=type_body)

            cohorts: list = CohortDAO.get_cohorts_in_id(cohorts_body)
            campuses: list = CampusDAO.get_campuses_in_id(campuses_body)
            for cohort in cohorts:
                new_event.cohorts.append(cohort)

            for campus in campuses:
                new_event.campuses.append(campus)

            EventDAO.save_event(new_event)

            return {'message': f'event {new_event.id} was created'}, 202
        else:
            return {'message': 'some parameters are missing'}, 400
    except Exception as e:
        print(f'error en create_event(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500


@event_blueprint.route('/events/<user_id>')
@swag_from('../flasgger/get_events_by_user.yml')
@jwt_required()
def get_events_by_user(user_id: int):
    try:
        events: list = db.session.query(Event).filter(User.id == user_id).join(User).all()

        return {'events': [element.to_json() for element in events]}, 200

    except Exception as e:
        print(f'error en get_events(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500
