from flask import Blueprint

bp = Blueprint('main', __name__)

from mvc.main import controller