from flask import request
from flask_login import current_user, login_required

from mvc_service_repository.tasks import bp
from mvc_service_repository.tasks.service import TaskService
from mvc_service_repository.tasks.view import TaskView

service = TaskService()
view = TaskView()


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    user_id = current_user.id
    match request.method:
        case 'GET':
            tasks = service.get_tasks(user_id=user_id)
            tasks = service.list_to_dict(task_list=tasks)
            return view.response(task_list=tasks)
        case 'POST':
            request_data = request.get_json()
            task = service.create_task(
                title=request_data['title'],
                description=request_data['description'],
                status=request_data['status'],
                user_id=user_id,
            )
            return view.response(task=task)


@bp.route('/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def task(task_id):
    user_id = current_user.id
    match request.method:
        case 'GET':
            task = service.get_task(task_id, user_id)
            return view.response(task=task)

        case 'PUT':
            request_data = request.get_json()
            status = request_data['status']
            title = request_data['title']
            description = request_data['description']

            task = service.update_task(
                task_id=task_id,
                status=status,
                title=title,
                description=description,
                user_id=user_id,
            )
            return view.response(task=task)

        case 'DELETE':
            task = service.delete_task(task_id, user_id)
            return view.response(task=task)
