from datetime import datetime

contract_types = [
    ContractType(name="Full-Time Employment", description="Full-time employment contract.", template="Full-time contract template content..."),
    ContractType(name="Part-Time Employment", description="Part-time employment contract.", template="Part-time contract template content..."),
    ContractType(name="Freelance Contract", description="Freelance contract.", template="Freelance contract template content...")
]
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=False)


class ContractType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    template = db.Column(db.Text, nullable=False)
