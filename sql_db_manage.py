#!/usr/bin/env python
from migrate.versioning.shell import main

from config.config_loader import core_config

if __name__ == '__main__':
    core_config.load()
    main(url=core_config.value_for('SQL_CONNECTION_URL'), debug='False', repository='db/db_migrate')
