import bcrypt

from daos.user_dao import UserDAO
from models.user import User


def authenticate(email, password):
    user: User = UserDAO.find_user_by_email(email)
    if user and bcrypt.checkpw(password.encode(), user.password.encode()):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserDAO.find_user_by_id(user_id)
