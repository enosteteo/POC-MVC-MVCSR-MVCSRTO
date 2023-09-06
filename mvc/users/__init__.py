from flask import Blueprint

bp = Blueprint('users', __name__)

from mvc.users import controller