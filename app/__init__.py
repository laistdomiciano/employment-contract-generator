from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "generator.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysupersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    from . models import User, Employee, Contract

    create_database(app)

    return app

def create_database(app):
    if not path.exixts('app/' + DB_NAME):
        db.create_alll(app=app)
        print('Created Database!')




















