import os

DATABASE_URL = 'generator.db'
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysupersecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost:5432/generator')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'myjwtsecretkey')
