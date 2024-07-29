from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    JWTManager(app)

    from .routes.auth import auth_bp
    from .routes.contract import contract_bp
    from .routes.employee import employee_bp
    from .routes.user import user_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(contract_bp, url_prefix='/contract')
    app.register_blueprint(employee_bp, url_prefix='/employee')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
