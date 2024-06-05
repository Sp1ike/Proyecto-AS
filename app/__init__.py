from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    api = Api(app)

    from .resources import ForoResource, ForoListResource
    api.add_resource(ForoListResource, '/api/foros')
    api.add_resource(ForoResource, '/api/foros/<int:id>')

    return app
