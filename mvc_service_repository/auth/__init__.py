from flask import Blueprint, jsonify, make_response, request, session
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from mvc_service_repository.users.model import User
from mvc_service_repository.users.service import UserService

bp = Blueprint('auth', __name__)
service = UserService()


@bp.route('/signup', methods=['POST'])
def signup():
    request_data = request.get_json()

    name = request_data['name']
    username = request_data['username']
    password = request_data['password']

    user = service.get_user_by_username(username)

    if user.__class__ is User:
        response = make_response(
            jsonify({'Error': 'User already exists'}), 409
        )
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response

    new_user = User(
        name=name,
        username=username,
        password=generate_password_hash(password, method='scrypt:32768:8:1'),
    )
    service.create_user(new_user)
    response = make_response(jsonify(new_user.to_dict()), 201)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Accept'] = 'application/json'
    return response


@bp.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()

    username = request_data['username']
    password = request_data['password']
    remember = True if request_data['remember'] else False

    user = service.get_user_by_username(username)

    if user.__class__ is Exception or not check_password_hash(
        user.password, password
    ):
        response = make_response(
            jsonify(
                {'Error': 'Please check your login details and try again'}
            ),
            401,
        )
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response
    session['logged_in'] = True
    session['user_id'] = user.id
    session['username'] = user.username
    login_user(user, remember=remember)
    response = make_response(jsonify(user.to_dict()), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Accept'] = 'application/json'
    return response


@bp.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('username', None)
    return 'Logout'
