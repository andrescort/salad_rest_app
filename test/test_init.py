from flask import Flask

def test_init_app(app, registers):
    assert isinstance(app, Flask)
    assert app.config["TESTING"] == False
    for _ in registers:
        assert _ in app.blueprints
