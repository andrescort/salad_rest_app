from flask import Blueprint, render_template

global_scope = Blueprint("views", __name__)

nav = [
    {"name": "Grupos", "url": "/api/groups"},
    {"name": "Contactos", "url": "/api/contacts"},
]


@global_scope.route("/", methods=['GET'])
def home():
    """Landing page route."""

    parameters = {"title": "Salad",
                  "NameLogo": "Salad app",
                  "description": "Web programming practice with Flask, it's an app that displays information"
                  }

    return render_template("home.html.jinja", nav=nav, **parameters)
