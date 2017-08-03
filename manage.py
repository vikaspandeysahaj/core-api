import os

from config.config_loader import core_config
from api.application import create_app


from api.blueprints import register_blueprints
from api.db_storage import storage


def devserver():
    config = core_config.load()
    app = create_app(config)
    register_blueprints(app)
    storage.init_storage(app.config, app)
    app.run(host='0.0.0.0', port=6060)

devserver()
