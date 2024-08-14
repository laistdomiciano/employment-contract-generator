from flask import Flask
import os
from app.models import db

DB_NAME = 'generator.db'
from app.routes import routes


def create_app():
    myapp = Flask(__name__)
    myapp.config['SECRET_KEY'] = 'mysupersecretkey'
    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(myapp)

    myapp.register_blueprint(routes, url_prefix='/')

    create_database(myapp)

    return myapp


def create_database(myapp):
    if not os.path.exists(DB_NAME):
        with myapp.app_context():
            db.create_all()
        print('Created Database!')


myapp = create_app()