import bcrypt
from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt import jwt_required

from daos.user_dao import UserDAO
from models.user import User
from validators.Validator import Validator

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/users')
@swag_from('../flasgger/get_users.yml')
@jwt_required()
def get_users():
    try:
        users: list = UserDAO.get_all_users()
        return {'users': [user.to_json() for user in users]}, 200
    except Exception as e:
        print(f'error en get_users(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500


@user_blueprint.route('/user/<user_id>')
@swag_from('../flasgger/get_user_by_id.yml')
@jwt_required()
def get_user_by_id(user_id: int):
    try:
        user: User = UserDAO.find_user_by_id(user_id)
        return {'result': user.to_json()}, 200
    except Exception as e:
        print(f'error en get_users(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500


@user_blueprint.route('/user', methods=['POST'])
@swag_from('../flasgger/create_user.yml')
def create_user():
    try:
        body_json: dict = request.json

        username: str = body_json.get('username') or ''
        email: str = body_json.get('email') or ''
        password_str: str = body_json.get('password') or ''

        create: bool = Validator.validate(username, email, password_str)

        if create:
            password_hashed = bcrypt.hashpw(password_str.encode(), bcrypt.gensalt())
            new_user: User = UserDAO.save_user(User(username=username, password=password_hashed, email=email))

            return {'message': f'user {new_user.id} has been created successfully'}, 202

        else:
            return {'message': 'some parameters are missing'}, 400

    except Exception as e:
        print(f'error en create_event(): {e}')
        return {'message': 'sorry, we are learning :v'}, 500
