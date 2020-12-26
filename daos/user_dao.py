import inspect

from config import db
from models.user import User


class UserDAO:

    @classmethod
    def find_user_by_email(cls, email: str) -> User:
        user: User = User.query.filter_by(email=email).first()
        return user

    @classmethod
    def find_user_by_id(cls, user_id: str) -> User:
        user: User = User.query.get(user_id)
        return user

    @classmethod
    def save_user(cls, user: User) -> User:
        if user:
            try:
                db.session.add(user)
                db.session.commit()
                return user
            except Exception as e:
                print(f'error en {cls.__name__}.{inspect.currentframe().f_code.co_name}(): {e}')
                return None

    @classmethod
    def get_all_users(cls):
        try:
            return User.query.all()
        except Exception as e:
            print(f'error en {cls.__name__}.{inspect.currentframe().f_code.co_name}(): {e}')
            return None
