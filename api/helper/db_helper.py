from sqlalchemy.exc import SQLAlchemyError
from api.db_storage import storage


def insert(record):
    try:
        results = storage.sql_db.session.add(record)
        storage.sql_db.session.commit()
        return results
    except SQLAlchemyError as e:
        print "ERROR: %s " % e.message
        storage.sql_db.session.rollback()
        raise


def delete(table, criteria):
    try:
        results = storage.sql_db.session.query(table).filter(criteria).delete()
        storage.sql_db.session.commit()
        return results
    except SQLAlchemyError as e:
        print "ERROR: %s " % e.message
        storage.sql_db.session.rollback()
        raise


def update(table, criteria, update_hash):
    try:
        results = storage.sql_db.session.query(table).filter(criteria).update(update_hash,synchronize_session=False)
        storage.sql_db.session.commit()
        return results
    except SQLAlchemyError as e:
        print "ERROR: %s " % e.message
        storage.sql_db.session.rollback()
        raise