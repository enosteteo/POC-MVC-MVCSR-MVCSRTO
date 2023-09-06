import uuid

from mvc_service_repository.users.model import User
from mvc_service_repository.users.repository import UserRepository

user_repository: UserRepository = UserRepository()


class UserService:
    def create_user(self, user: User) -> User:
        if user_repository.find_by_username(user.username):
            return Exception(f'User {user.username} already exists')
        return user_repository.create(user)

    def get_user(self, user_id: uuid.UUID):
        return user_repository.find_by_id(user_id)

    def get_all_users(self) -> list[User]:
        return user_repository.get_all()

    def list_to_dict(self, user_list: list[User]) -> dict:
        return {
            'users': [
                {i: user_list[i].to_dict()} for i in range(len(user_list))
            ]
        }

    def update_user(self, user_id: uuid.UUID, user: User):
        if user_repository.find_by_id(user_id):
            return Exception(f'User {user_id} not found')
        if user_repository.find_by_username(user.username).id != user_id:
            return Exception(f'User {user.username} already exists')
        user = user_repository.update(user_id, user)

    def delete_user(self, user_id: uuid.UUID):
        if not user_repository.find_by_id(user_id):
            return Exception(f'User {user_id} not found')
        return user_repository.delete(user_id)

    def get_user_by_username(self, username: str):
        user = user_repository.find_by_username(username)
        if user is None:
            return Exception(f'User {username} not found')
        return user
