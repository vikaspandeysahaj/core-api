from flask_sqlalchemy import SQLAlchemy

class UnLockedAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        if not "isolation_level" in options:
            options["isolation_level"] = "READ COMMITTED"
        return super(UnLockedAlchemy, self).apply_driver_hacks(app, info, options)


class DbStorage():
    exist_db = None
    sql_db = UnLockedAlchemy()

    def init_storage(self, config, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = config['SQL_CONNECTION_URL']
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.sql_db.init_app(app)
        app.app_context().push()

storage = DbStorage()