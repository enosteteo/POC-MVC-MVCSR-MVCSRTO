from flask import Blueprint

bp = Blueprint('users', __name__)

from mvc_service_repository_transferobject.users import controller
