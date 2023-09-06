import uuid

from mvc_service_repository_transferobject.extensions import db
from mvc_service_repository_transferobject.users.model import User
from mvc_service_repository_transferobject.users.user_to import UserTO


class UserRepository:
    def create(self, user: User) -> UserTO:
        db.session.add(user)
        db.session.commit()
        return UserTO(user.id, user.name, user.username)

    def find_by_id(self, user_id: uuid.UUID):
        user = db.session.query(User).filter(User.id == user_id).first()
        if user:
            return UserTO(user.id, user.name, user.username, user.tasks)
        return None

    def get_all(self) -> list[UserTO]:
        users: list[User] = User.query.all()
        return [
            UserTO(user.id, user.name, user.username, user.tasks)
            for user in users
        ]

    def update(self, user_id: uuid.UUID, user: User):
        user = db.session.query(User).filter(User.id == user_id).update(user)
        return UserTO(user.id, user.name, user.username, user.tasks)

    def delete(self, user_id: uuid.UUID):
        user = db.session.query(User).filter(User.id == user_id).first()
        db.session.delete(user)
        db.session.commit()
        return UserTO(user.id, user.name, user.username, user.tasks)

    def find_by_username(self, username: str):
        user = db.session.query(User).filter(User.username == username).first()
        return user
