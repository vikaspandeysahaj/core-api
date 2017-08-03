import uuid

from sqlalchemy import Column, Integer, String

from api.db_storage import storage
from api.helper.db_helper import insert


class Role(storage.sql_db.Model):

    USER = 'user'
    SELLER = 'seller'
    ADMIN = 'admin'

    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(String(100))
    title = Column(String(100))

    def __init__(self,
                 role_id,
                 title=None):

        self.role_id = role_id
        self.title = title

    def as_json(self):
        property_hash = {
            'role_id':self.role_id,
            'title': self.title
        }
        return property_hash

    @classmethod
    def create_role(cls, title):
        role = Role(role_id= uuid.uuid1().hex,
                    title=title)
        insert(role)
        created_role = Role.query.filter(Role.role_id == role.role_id).all()
        return created_role[0] if created_role is not None else None

    @staticmethod
    def is_valid_hash_for_create(role_hash):
        errors = []
        name = role_hash['title']
        errors.append({"title": "title cannot be blank"}) if not name else None

        if not errors:
            return True
        else:
            raise ValueError(errors)

    @classmethod
    def find_by_id(cls, role_id):
        results = Role.query.filter(Role.role_id == role_id).all()
        return results[0] if results.__len__() > 0 else None

    @classmethod
    def find_by_title(cls, title):
        results = Role.query.filter(Role.title == title).all()
        return results[0] if results.__len__() > 0 else None
