from flask import Flask
from backend.app.models import db
from flask_jwt_extended import JWTManager
from backend.app.routes import routes
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    myapp = Flask(__name__)
    myapp.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysupersecretkey')
    myapp.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'postgresql://username:password@localhost/generator_db')
    myapp.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'mysupersecretjwtkey')

    db.init_app(myapp)

    JWTManager(myapp)
    myapp.register_blueprint(routes, url_prefix='/')
  # Run migrations or create tables if needed
    with myapp.app_context():
        db.create_all()
    return myapp


myapp = create_app()