from flask_login import current_user, login_required

from mvc_service_repository_transferobject.users import bp
from mvc_service_repository_transferobject.users.service import UserService
from mvc_service_repository_transferobject.users.view import UserView

service = UserService()
view = UserView()


@bp.route('/', methods=['GET'])
@login_required
def index():
    users = service.get_all_users()
    users = service.list_to_dict(users)
    return view.response(user_list=users)


@bp.route('/', methods=['DELETE'])
@login_required
def delete():
    user = service.delete_user(current_user.id)
    return view.response(user=user, status_code=202)
