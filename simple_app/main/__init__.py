from flask import Blueprint

main = Blueprint('main', __name__, static_folder="../Public", template_folder="../View", static_url_path="/")

from . import routes, events