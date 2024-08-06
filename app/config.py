import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/contract_generator_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysupersecretkey')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'superjwtsecretkey')


    #https://employment-contract-generator.com
