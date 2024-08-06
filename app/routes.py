from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, create_access_token
from models import User, Employee, ContractType, TokenBlocklist, db

routes = Blueprint('routes', __name__)

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            return render_template('signup.html', error="Username already taken")

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('api.login'))

    return render_template('signup.html')

@routes.route('/login', methods=['POST'])
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


@routes.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()
    return jsonify(msg="Successfully logged out"), 200

@routes.route('/form')
@jwt_required()
def form():
    return render_template('form.html')


# @routes.route('/contract_types', methods=['GET'])
# @jwt_required()
# def get_contract_types():
#     contract_types = ContractType.query.all()
#     pass
#
# @routes.route('/contracts', methods=['POST'])
# @jwt_required()
# def create_contract():
#     data = request.json
#     pass
#
# # Here you would generate the PDF and return it.


