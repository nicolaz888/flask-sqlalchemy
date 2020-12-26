import inspect

from config import db
from models.cohort import Cohort


class CohortDAO:

    @classmethod
    def get_cohorts_in_id(cls, cohorts: list) -> list:
        if cohorts:
            try:
                return db.session.query(Cohort).filter(Cohort.id.in_(cohorts))

            except Exception as e:
                print(f'error en {cls.__name__}.{inspect.currentframe().f_code.co_name}(): {e}')
                return []
        else:
            return []
