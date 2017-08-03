import os
import sys
from sqlalchemy import create_engine

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/../..")
from config.config_loader import core_config

def run_migrations():
    env = os.environ['API_ENV'].title() if os.environ.get('API_ENV') else "Development"
    root_connection_url = core_config.value_for("ROOT_CONNECTION_URL")
    db_name = core_config.value_for("SQL_DB_NAME")
    db_user = core_config.value_for("SQL_DB_USERNAME")
    password = core_config.value_for("SQL_DB_PASSWORD")
    root_password = core_config.value_for("SQL_ROOT_PASSWORD")

    print("******************************")
    print("Reseting {env} DB. {db_name} and {db_user}".format(db_user=db_user, db_name=db_name, env=env))
    print("******************************")
    reset_migrations = [
        "DROP DATABASE {db_name}".format(db_name=db_name),
        "CREATE DATABASE {db_name}".format(db_name=db_name),
        "DROP USER '{db_user}'@'localhost'".format(db_user=db_user),
        "CREATE USER {db_user}@'localhost' IDENTIFIED BY '{password}'".format(db_user=db_user, password=password),
        "GRANT ALL ON {db_name}.* TO '{db_user}'@'localhost'".format(db_user=db_user, db_name=db_name)
    ]

    engine = create_engine(root_connection_url)
    with engine.connect() as con:
        for statement in reset_migrations:
            con.execute(statement)


if __name__ == "__main__":
    core_config.load()
    run_migrations()
