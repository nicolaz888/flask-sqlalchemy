import inspect

from config import db
from models.campus import Campus


class CampusDAO:

    @classmethod
    def get_campuses_in_id(cls, cohorts: list) -> list:
        if cohorts:
            try:
                return db.session.query(Campus).filter(Campus.id.in_(cohorts))

            except Exception as e:
                print(f'error en {cls.__name__}.{inspect.currentframe().f_code.co_name}(): {e}')
                return []
        else:
            return []
