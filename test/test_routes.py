from flask import Flask, render_template
import pytest

from tu_modulo.routes import global_scope, home


@pytest.fixture
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.register_blueprint(global_scope)

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Salad app" in response.data
    assert b"Web programming practice with Flask" in response.data
    assert b"Grupos" in response.data
    assert b"/api/groups" in response.data
    assert b"Contactos" in response.data
    assert b"/api/contacts" in response.data



