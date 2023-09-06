import uuid

from flask_login import current_user, login_required

from mvc.extensions import db
from mvc.users import bp
from mvc.users.model import User
from mvc.users.view import UserView

view = UserView()


@bp.route('/', methods=['GET'])
@login_required
def index():
    users = get_all_users()
    users = list_to_dict(users)
    return view.response(user_list=users)


@bp.route('/', methods=['DELETE'])
@login_required
def delete():
    user = delete_user(current_user.id)
    return view.response(user=user, status_code=202)


def find_by_id(user_id: uuid.UUID):
    user = db.session.query(User).filter(User.id == user_id).first()
    if user:
        return user
    return None


def update(user_id: uuid.UUID, user: User):
    user = db.session.query(User).filter(User.id == user_id).update(user)
    return user


def delete(user_id: uuid.UUID):
    user = db.session.query(User).filter(User.id == user_id).first()
    db.session.delete(user)
    db.session.commit()
    return user


def find_by_username(username: str):
    user = db.session.query(User).filter(User.username == username).first()
    return user


def create_user(user: User) -> User:
    if find_by_username(user.username):
        return Exception(f'User {user.username} already exists')
    db.session.add(user)
    db.session.commit()
    return user


def get_user(user_id: uuid.UUID):
    return find_by_id(user_id)


def get_all_users() -> list[User]:
    users: list[User] = db.session.query(User).all()
    return [user for user in users]


def list_to_dict(user_list: list[User]) -> dict:
    return {
        'users': [{i: user_list[i].to_dict()} for i in range(len(user_list))]
    }


def update_user(user_id: uuid.UUID, user: User):
    if find_by_id(user_id):
        return Exception(f'User {user_id} not found')
    if find_by_username(user.username).id != user_id:
        return Exception(f'User {user.username} already exists')
    user = update(user_id, user)


def delete_user(user_id: uuid.UUID):
    if not find_by_id(user_id):
        return Exception(f'User {user_id} not found')
    return delete(user_id)


def get_user_by_username(username: str):
    user = find_by_username(username)
    if user is None:
        return Exception(f'User {username} not found')
    return user
