class Config:
    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"

class DevConfigs:
    SERVER_NAME = "0.0.0.0:8080"
    DEBUG = True

config: dict = {"development": DevConfigs}
