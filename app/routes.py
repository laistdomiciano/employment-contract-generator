from flask import Blueprint, request, render_template, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt, create_access_token
# from models import User, Employee, ContractType, TokenBlocklist, db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    # return <h1>Employment Contract Generator</h1>
    return render_template('home.html')


@routes.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Authentication logic here
        if username != 'admin' or password != 'secret':
            error = 'Invalid credentials'
        else:
            return redirect(url_for('routes.home'))
    return render_template('login.html', error=error)


@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic here
        pass
    return render_template('signup.html')

#     data = request.json
#     username = data.get('username')
#     password = data.get('password')
#     user = User.query.filter_by(username=username).first()
#
#     if user and user.check_password(password):
#         access_token = create_access_token(identity={'username': user.username})
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({"msg": "Wrong username or password. Try again"}), 401

# @routes.route('/signup') #methods=['GET', 'POST'])
# def signup():
#     return "<h1>Sign Up</h1>"
#     return render_template('signup.html')
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#
#         if User.query.filter_by(username=username).first():
#             return render_template('signup.html', error="Username already taken")
#
#         hashed_password = generate_password_hash(password)
#         new_user = User(username=username, password_hash=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#
#         return redirect(url_for('api.login'))
#
#     return render_template('signup.html')
#


@routes.route('/logout') #, methods=['POST'])
# @jwt_required()
def logout():
    return "<h1>Logout</h1>"
#     jti = get_jwt()["jti"]
#     db.session.add(TokenBlocklist(jti=jti))
#     db.session.commit()
#     return jsonify(msg="Successfully logged out"), 200
#

@routes.route('/form')
# @jwt_required
def form():
    return "<h1>Employment Contract Generator - This would be the dashboard</h1>"
        #(render_template('form.html'))


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


