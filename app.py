from flask_jwt import JWT
from blueprints.campus_blueprint import campus_blueprint
from blueprints.event_blueprint import event_blueprint
from blueprints.user_blueprint import user_blueprint
from config import app, db
from security import authenticate, identity

from models.user import User
from models.campus import Campus
from models.event_type import EventType
from models.event import Event
from models.cohort import Cohort

jwt = JWT(app, authenticate, identity)

app.register_blueprint(user_blueprint)
app.register_blueprint(event_blueprint)
app.register_blueprint(campus_blueprint)

if __name__ == "__main__":
    db.create_all()

    app.run()
