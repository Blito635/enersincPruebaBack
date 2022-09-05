from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)

banca.add_url_rule(
    '/persona', view_func=controllers.cruDoctor, methods=['GET', 'POST', 'PUT','DELETE'])




