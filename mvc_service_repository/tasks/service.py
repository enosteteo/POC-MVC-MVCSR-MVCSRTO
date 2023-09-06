from mvc_service_repository.tasks.model import Task
from mvc_service_repository.tasks.repository import TaskRepository

repository = TaskRepository()


class TaskService:
    def create_task(self, title, description, user_id, status='TODO'):
        task: Task = Task(title, description, status, user_id)
        return repository.create(task)

    def get_task(self, task_id, user_id):
        task = repository.find_by_task_id_and_user_id(task_id, user_id)
        return task

    def update_task(self, task_id, status, title, description, user_id):
        task = Task(title, description, status, user_id)

        if task.status not in ['TODO', 'DOING', 'DONE']:
            return Exception('Invalid status')
        task = repository.update(task_id, user_id, task)

        return task

    def delete_task(self, task_id, user_id):
        task = repository.delete(user_id=user_id, task_id=task_id)
        return task

    def get_tasks(self, user_id):
        tasks: list[Task] = repository.get_all(user_id=user_id)

        return tasks

    def list_to_dict(self, task_list: list[Task]) -> dict:
        return {
            'tasks': [
                {i: task_list[i].to_dict()} for i in range(len(task_list))
            ]
        }
