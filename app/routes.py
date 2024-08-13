from flask import Blueprint, request, render_template, redirect, url_for,flash
from models import *
from werkzeug.security import generate_password_hash, check_password_hash

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
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        passoword2 = request.form.get('password1')

        if len(email) < 8:
            flash('Email must be greater than 8 characters.', category='error')
        if len(name) < 8:
            flash('Name must be greater than 8 characters.', category='error')
        elif len(username) < 5:
            flash('Username must be greater than 5 characters.', category='error')
        elif len(password1) < 4:
            flash('Username must be greater than 4 characters.', category='error')
        elif password1 != passoword2 :
            flash('Password do not match', category='error')
        else:
            new_user = User(email=Email, username=Username, name=Name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success')
            return redirect(url_for('routes.home'))

    return render_template('signup.html')


@routes.route('/logout') #, methods=['POST'])
def logout():
    return "<h1>Logout</h1>"
#     jti = get_jwt()["jti"]
#     db.session.add(TokenBlocklist(jti=jti))
#     db.session.commit()
#     return jsonify(msg="Successfully logged out"), 200


@routes.route('/dashboard')
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


