from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    myapp = Flask(__name__)

    myapp.config.from_object('app.config.Config')

    db.init_app(myapp)
    migrate.init_app(myapp, db)
    jwt.init_app(myapp)

    from app.routes import routes_bp
    myapp.register_blueprint(routes_bp)

    return myapp
