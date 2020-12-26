import inspect

from config import db
from models.event import Event


class EventDAO:

    @classmethod
    def save_event(cls, event: Event) -> Event:
        if event:
            try:
                db.session.add(event)
                db.session.commit()
                return event
            except Exception as e:
                print(f'error en {cls.__name__}.{inspect.currentframe().f_code.co_name}(): {e}')
                return None
