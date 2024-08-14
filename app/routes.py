from flask import Blueprint
routes = Blueprint('routes', __name__)
from flask import Blueprint
from .models import User, Employee, ContractType, Contract, db
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html')


# Authentication routes
@routes.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)


@routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', hide_buttons=True)


# Contract creation (only accessible with JWT)
@routes.route('/create-contract', methods=['POST'])
@jwt_required()
def create_contract():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_contract = Contract(user_id=user_id, employee_id=data['employee_id'], contract_type_id=data['contract_type_id'], contract_json=json.dumps(data['contract_json']))
    db.session.add(new_contract)
    db.session.commit()
    return jsonify({'message': 'Contract created successfully'}), 201


# PDF Generation
@routes.route('/contract-pdf/<int:contract_id>', methods=['GET'])
@jwt_required()
def generate_contract_pdf(contract_id):
    contract = Contract.query.get(contract_id)
    if not contract:
        return jsonify({'message': 'Contract not found'}), 404

    # Create a PDF from JSON
    c = canvas.Canvas(f"contract_{contract_id}.pdf", pagesize=letter)
    c.drawString(100, 750, f"Contract ID: {contract.id}")
    c.drawString(100, 735, f"User ID: {contract.user_id}")
    c.drawString(100, 720, f"Employee ID: {contract.employee_id}")
    c.drawString(100, 705, f"Contract Type ID: {contract.contract_type_id}")

    contract_data = json.loads(contract.contract_json)
    y = 690
    for key, value in contract_data.items():
        c.drawString(100, y, f"{key}: {value}")
        y -= 15

    c.save()
    return jsonify({'message': 'PDF generated successfully'}), 200


