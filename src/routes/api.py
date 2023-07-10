from flask import Blueprint, render_template

api_scope = Blueprint("api", __name__)


@api_scope.route("/", methods=['GET'])
def products():
    """Landing page api."""

    return "Api Products"#render_template("layout.html")
