from flask import Response, jsonify, make_response

from mvc_service_repository_transferobject.tasks.model import Task


class TaskView:
    def response(
        self,
        task: Task = None,
        task_list: list[Task] = None,
        status_code=200,
    ) -> Response:
        if task.__class__ is Exception or task_list.__class__ is Exception:
            response = make_response(
                jsonify(
                    {
                        'Error': f'{task if task.__class__==Exception else task_list}'
                    }
                ),
                400,
            )

        elif task:
            response = make_response(jsonify(task.to_dict()), status_code)
        elif task_list:
            response = make_response(jsonify(task_list), status_code)
        else:
            response = make_response(jsonify({'Error': 'Bad request'}), 400)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response
