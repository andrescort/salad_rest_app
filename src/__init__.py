from flask import Flask
from configs import Config

from .routes import global_scope, api_scope#, errors_scope

def init_app(conf):
    app = Flask(__name__,
            static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(conf)
    app.register_blueprint(global_scope, url_prefix="/")
    app.register_blueprint(api_scope, url_prefix="/api")
    return app

#app.register_blueprint(errors_scope, url_prefix="/")

