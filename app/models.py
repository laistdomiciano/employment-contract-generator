from flask_login import UserMixin
from . import db
from enum import Enum


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(100))

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    position = db.Column(db.String(150))
    department = db.Column(db.String(100))
    contracts = db.relationship('Contract')


class ContractType(Enum):
    FREELANCE = "freelance"
    FULL_TIME = "full-time"
    PART_TIME = "part-time"


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.Text)
    type = db.Column(db.Enum(ContractType))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
