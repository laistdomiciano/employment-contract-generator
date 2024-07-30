from datetime import datetime

contract_types = [
    ContractType(name="Full-Time Employment", description="Full-time employment contract.", template="Full-time contract template content..."),
    ContractType(name="Part-Time Employment", description="Part-time employment contract.", template="Part-time contract template content..."),
    ContractType(name="Freelance Contract", description="Freelance contract.", template="Freelance contract template content...")
]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    hire_date = db.Column(db.DateTime, default=datetime.utcnow)

class ContractType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    template = db.Column(db.Text, nullable=False)