from flask import Response, jsonify, make_response

from mvc_service_repository.users.model import User


class UserView:
    def response(
        self,
        user: User = None,
        user_list: list[User] = None,
        status_code=200,
    ) -> Response:
        if user:
            response = make_response(jsonify(user.to_dict()), status_code)
        elif user_list:
            response = make_response(jsonify(user_list), status_code)
        else:
            response = make_response(jsonify({'Error': 'Bad request'}), 400)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response
