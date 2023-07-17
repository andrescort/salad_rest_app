from flask import Blueprint, render_template

Home = Blueprint("views", __name__)

nav = [
    {"name": "Home", "icon": "home", "url": "/"},
    {"name": "Menu", "icon": "book", "url": "/Menu"},
    {"name": "Order", "icon": "restaurant", "url": "/order"},
    {"name": "Likes", "icon": "heart", "url": "/likes"},
    {"name": "User", "icon": "person", "url": "/User"},
]


@Home.route("/", methods=['GET'])
def home():
    """Landing page Home."""

    parameters = {"title": "Salad",
                  "NameLogo": "Salad app"
                  }

    return render_template("home.html.jinja", nav=nav, **parameters)
