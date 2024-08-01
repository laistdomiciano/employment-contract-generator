from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import User, Employee, ContractType, db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('api', __name__)


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()
    return jsonify(msg="Successfully logged out"), 200


@bp.route('/contracts', methods=['POST'])
@jwt_required()
def create_contract():
    data = request.json
    contract_type_id = data.get('contract_type_id')
    employee_id = data.get('employee_id')
    company_name = data.get('company_name', 'Your Company Name')
    salary = data.get('salary', 'Negotiable')
    benefits = data.get('benefits', 'Standard Benefits')
    hourly_rate = data.get('hourly_rate', 'Negotiable')
    project_fee = data.get('project_fee', 'Negotiable')
    payment_terms = data.get('payment_terms', 'Upon Completion')

    contract_type = ContractType.query.get(contract_type_id)
    employee = Employee.query.get(employee_id)

    if not contract_type or not employee:
        return jsonify({"msg": "Invalid contract type or employee"}), 400

    contract_content = contract_type.template.format(
        employee_name=employee.name,
        employee_position=employee.position,
        employee_department=employee.department,
        company_name=company_name,
        salary=salary,
        benefits=benefits,
        hourly_rate=hourly_rate,
        project_fee=project_fee,
        payment_terms=payment_terms
    )

    # Generate PDF logic would go here
    # For now, we'll just return the contract content as a placeholder
    return jsonify(contract=contract_content), 200
