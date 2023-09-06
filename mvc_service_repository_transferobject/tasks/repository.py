from mvc_service_repository_transferobject.extensions import db
from mvc_service_repository_transferobject.tasks.model import Task


class TaskRepository:
    def create(self, task: Task) -> Task:
        db.session.add(task)
        db.session.commit()
        return task

    def find_by_task_id_and_user_id(self, task_id, user_id) -> Task | None:
        task = (
            db.session.query(Task)
            .filter_by(user_id=user_id, id=task_id)
            .first_or_404()
        )
        if task.__class__ is Task:
            return task
        return task

    def update(self, task_id, user_id, task: Task) -> Task:
        task_db = (
            db.session.query(Task)
            .filter_by(user_id=user_id, id=task_id)
            .first_or_404()
        )
        task_db.title = task.title
        task_db.description = task.description
        task_db.status = task.status
        db.session.commit()
        return task_db

    def delete(self, task_id, user_id) -> Task:
        task = (
            db.session.query(Task)
            .filter_by(user_id=user_id, id=task_id)
            .first_or_404()
        )
        db.session.delete(task)
        db.session.commit()
        return task

    def get_all(self, user_id) -> list[Task]:
        tasks: list[Task] = (
            db.session.query(Task).filter_by(user_id=user_id).all()
        )
        return tasks
