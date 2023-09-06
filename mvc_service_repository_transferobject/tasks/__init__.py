from flask import Blueprint

bp = Blueprint('tasks', __name__)

from mvc_service_repository_transferobject.tasks import controller
