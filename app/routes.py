from flask import Blueprint, request, render_template, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt, create_access_token
# from models import User, Employee, ContractType, TokenBlocklist, db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
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
    # if request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #
    #     if User.query.filter_by(username=username).first():
    #         return render_template('signup.html', error="Username already taken")
    #
    # hashed_password = generate_password_hash(password)
    # new_user = User(username=username, password_hash=hashed_password)
    # db.session.add(new_user)
    # db.session.commit()
    #     return redirect(url_for('routes.login'))
    return render_template('signup.html')


@routes.route('/logout') #, methods=['POST'])
# @jwt_required()
def logout():
    return "<h1>Logout</h1>"
#     jti = get_jwt()["jti"]
#     db.session.add(TokenBlocklist(jti=jti))
#     db.session.commit()
#     return jsonify(msg="Successfully logged out"), 200


@routes.route('/dashboard')
# @jwt_required
def dashboard():
    return render_template('dashboard.html')


# @routes.route('/contract_types', methods=['GET'])
# @jwt_required()
# def get_contract_types():
#     contract_types = ContractType.query.all()
#     pass


# @routes.route('/contracts', methods=['POST'])
# @jwt_required()
# def create_contract():
#     data = request.json
#     pass



# # Here you would generate the PDF and return it.


