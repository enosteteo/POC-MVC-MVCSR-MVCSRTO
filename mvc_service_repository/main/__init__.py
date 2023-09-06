from flask import Blueprint

bp = Blueprint('main', __name__)

from mvc_service_repository.main import controller
