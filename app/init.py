from flask import Flask
import os
from app.models import db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from app.routes import routes


DB_NAME = 'generator.db'



def create_app():
    myapp = Flask(__name__)
    myapp.config['SECRET_KEY'] = 'mysupersecretkey'
    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    myapp.config['JWT_TOKEN_LOCATION'] = ['headers']

    db.init_app(myapp)
    JWTManager(myapp)

    myapp.register_blueprint(routes, url_prefix='/')

    create_database(myapp)

    return myapp


def create_database(myapp):
    if not os.path.exists(DB_NAME):
        with myapp.app_context():
            db.create_all()
        print('Created Database!')


myapp = create_app()