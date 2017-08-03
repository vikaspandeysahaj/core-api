import contextlib
import os
import sys
from unittest import TestCase

import requests

from config.config_loader import core_config
from api.application import create_app
from api.blueprints import register_blueprints
from api.db_storage import storage

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/..")


def fixture_path_for(name):
    return current_path + "/support/fixtures/{filename}".format(filename=name)


class UnitTest(TestCase):
    def setUp(self):
        print("Test setup")
        os.environ['API_ENV'] = "Test"
        config = core_config.load()
        self.app = create_app(config)
        storage.init_storage(config, self.app)
        self.reset_db(config)

    def app(self):
        return self.app

    def tearDown(self):
        print("Test tear Down")
        self.reset_db(core_config.load())

    def fixture_path(self, filename):
        return fixture_path_for(filename)

    def reset_db(self, config):
        print("Database reset")
        meta = storage.sql_db.metadata
        for table in reversed(meta.sorted_tables):
            storage.sql_db.session.execute(table.delete())
            storage.sql_db.session.commit()

class ServiceTest(UnitTest):
    def setUp(self):
        os.environ['API_ENV'] = "Test"
        config = core_config.load()
        base_app = create_app(config)
        register_blueprints(base_app)
        storage.init_storage(config, base_app)
        self.app = base_app.test_client()
        self.reset_db(base_app.config)

    def tearDown(self):
        print("Test tear Down")
        self.reset_db(core_config.load())

    def reset_db(self, config):
        print("Database reset")
        meta = storage.sql_db.metadata
        for table in reversed(meta.sorted_tables):
            storage.sql_db.session.execute(table.delete())
            storage.sql_db.session.commit()
