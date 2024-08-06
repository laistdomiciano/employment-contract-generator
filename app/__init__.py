from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config
from .models import db, TokenBlocklist
from .routes import *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysupersecretkey'

    from .routes import routes
    # from .auth import auth
    app.register_blueprint(routes, url_prefix='/')

    return app

    # app.config.from_object(Config)
    #
    # db.init_app(app)
    # migrate = Migrate(app, db)
    # jwt = JWTManager(app)
    #
    # @jwt.token_in_blocklist_loader
    # def check_if_token_revoked(jwt_header, jwt_payload):
    #     jti = jwt_payload["jti"]
    #     token = TokenBlocklist.query.filter_by(jti=jti).first()
    #     return token is not None
    #
    # from . import routes
    # app.register_blueprint(routes.routes)
    #
    # return app