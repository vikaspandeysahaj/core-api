from werkzeug.utils import import_string


class AppConfigParser():

    def __init__(self, config_module="config.app_config.%s"):
        self.config_module = config_module

    def load_config(self, config_env):
        string_types = (str, unicode)
        config = {}
        if isinstance(config_env, string_types):
            config_env = import_string(self.config_module % config_env)
            for key in dir(config_env):
                if key.isupper():
                    config[key] = getattr(config_env, key)
        return config
