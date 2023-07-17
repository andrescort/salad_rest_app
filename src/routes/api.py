from flask import Blueprint

api = Blueprint("api", __name__)


@api.route("/", methods=['GET'])
def products():
    """Landing page api."""

    return "Api Products"
