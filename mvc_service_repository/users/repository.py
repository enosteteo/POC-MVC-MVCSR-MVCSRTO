import uuid

from mvc_service_repository.extensions import db
from mvc_service_repository.users.model import User


class UserRepository:
    def create(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    def find_by_id(self, user_id: uuid.UUID):
        user = db.session.query(User).filter(User.id == user_id).first()
        if user:
            return user
        return None

    def get_all(self) -> list[User]:
        users: list[User] = User.query.all()
        return [user for user in users]

    def update(self, user_id: uuid.UUID, user: User):
        user = db.session.query(User).filter(User.id == user_id).update(user)
        return user

    def delete(self, user_id: uuid.UUID):
        user = db.session.query(User).filter(User.id == user_id).first()
        db.session.delete(user)
        db.session.commit()
        return user

    def find_by_username(self, username: str):
        user = db.session.query(User).filter(User.username == username).first()
        return user
