import os

from config.config_parser import AppConfigParser


class coreConfig:
    def __init__(self):
        self.config = None

    def load(self):
        config_env = os.environ['API_ENV'].title() if os.environ.get('API_ENV') else "Development"
        self.config = AppConfigParser().load_config(config_env)
        return self.config

    def value_for(self, key):
        return self.config[key]


core_config = coreConfig()
