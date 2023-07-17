from flask import Flask
from configs import Config

from .routes import Home

def init_app(conf):
    app = Flask(__name__,
            static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(conf)
    app.register_blueprint(Home, url_prefix="/")
    return app
