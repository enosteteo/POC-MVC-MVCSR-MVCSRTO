from flask import Blueprint

bp = Blueprint('tasks', __name__)

from mvc_service_repository.tasks import controller
