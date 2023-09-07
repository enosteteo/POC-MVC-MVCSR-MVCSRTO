from flask import request
from flask_login import current_user, login_required

from mvc.extensions import db
from mvc.tasks import bp
from mvc.tasks.model import Task
from mvc.tasks.view import TaskView

view = TaskView()


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    user_id = current_user.id
    match request.method:
        case 'GET':
            tasks = get_tasks(user_id=user_id)
            tasks = list_to_dict(task_list=tasks)
            return view.response(task_list=tasks)
        case 'POST':
            request_data = request.get_json()
            task = create_task(
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
            task = get_task(task_id, user_id)
            return view.response(task=task)

        case 'PUT':
            request_data = request.get_json()
            status = request_data['status']
            title = request_data['title']
            description = request_data['description']

            task = update_task(
                task_id=task_id,
                status=status,
                title=title,
                description=description,
                user_id=user_id,
            )
            return view.response(task=task)

        case 'DELETE':
            task = delete_task(task_id, user_id)
            return view.response(task=task)


def list_to_dict(task_list: list[Task]) -> dict:
    return {
        'tasks': [{i: task_list[i].to_dict()} for i in range(len(task_list))]
    }


def create_task(title, description, user_id, status='TODO'):
    task: Task = Task(title, description, status, user_id)
    db.session.add(task)
    db.session.commit()
    return task


def get_task(task_id, user_id):
    task = (
        db.session.query(Task)
        .filter_by(user_id=user_id, id=task_id)
        .first_or_404()
    )
    return task


def update_task(task_id, status, title, description, user_id):
    task = Task(title, description, status, user_id)

    if task.status not in ['TODO', 'DOING', 'DONE']:
        return Exception('Invalid status')

    task_db = (
        db.session.query(Task)
        .filter_by(user_id=user_id, id=task_id)
        .first_or_404()
    )
    task_db.title = task.title
    task_db.description = task.description
    task_db.status = task.status
    db.session.commit()

    return task


def delete_task(task_id, user_id):
    task = (
        db.session.query(Task)
        .filter_by(user_id=user_id, id=task_id)
        .first_or_404()
    )
    db.session.delete(task)
    db.session.commit()
    return task


def get_tasks(user_id):
    tasks: list[Task] = db.session.query(Task).filter_by(user_id=user_id).all()

    return tasks
