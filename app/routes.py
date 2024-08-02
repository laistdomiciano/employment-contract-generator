from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, create_access_token
from .models import User, Employee, ContractType, TokenBlocklist, db

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
        return jsonify({"msg": "Wrong username or password. Try again"}), 401


@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()
    return jsonify(msg="Successfully logged out"), 200


@bp.route('/contract_types', methods=['GET'])
@jwt_required()
def get_contract_types():
    contract_types = ContractType.query.all()
    pass

@bp.route('/contracts', methods=['POST'])
@jwt_required()
def create_contract():
    data = request.json
    pass

# Here you would generate the PDF and return it.


