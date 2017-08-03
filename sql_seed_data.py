import hashlib
from sqlalchemy import Table, MetaData
from config.config_loader import core_config
from api.application import create_app
from api.db_storage import storage

config = core_config.load()
app = create_app(config)
storage.init_storage(config, app)

meta = MetaData()
migrate_engine = storage.sql_db.engine
meta.bind = migrate_engine
connection = migrate_engine.connect()

role = Table('role',meta,autoload = True, autoload_with=migrate_engine)
category = Table('category',meta,autoload = True, autoload_with=migrate_engine)

# Clean database
connection.execute(role.delete())
connection.execute(category.delete())

# Seed value for role
connection.execute(role.insert().values(role_id=1, title="user"))
connection.execute(role.insert().values(role_id=2, title="seller"))
connection.execute(role.insert().values(role_id=3, title="admin"))


# Seed value for category
connection.execute(category.insert().values(category_id=1, title="fashion"))
connection.execute(category.insert().values(category_id=2, title="food"))
connection.execute(category.insert().values(category_id=3, title="grocery"))
connection.execute(category.insert().values(category_id=4, title="kids"))
connection.execute(category.insert().values(category_id=5, title="electronics"))


