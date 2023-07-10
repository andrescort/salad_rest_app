from configs import DevConfigs
from src import init_app

from test import test_init_app

conf = DevConfigs
app = init_app(conf)

if __name__ == '__main__':
    # test_init_app(app)
    app.run()
