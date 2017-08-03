import uuid

from sqlalchemy import Column, Integer, String

from api.db_storage import storage
from api.helper.db_helper import insert


class Category(storage.sql_db.Model):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(String(100))
    title = Column(String(100))

    def __init__(self,
                 category_id,
                 title=None):

        self.category_id = category_id
        self.title = title

    def as_json(self):
        property_hash = {
            'category_id':self.category_id,
            'title': self.title
        }
        return property_hash

    @classmethod
    def create_category(cls, title):
        category = Category(category_id= uuid.uuid1().hex,
                    title=title)
        insert(category)
        created_category = Category.query.filter(Category.category_id == category.category_id).all()
        return created_category[0] if created_category is not None else None

    @staticmethod
    def is_valid_hash_for_create(category_hash):
        errors = []
        name = category_hash['title']
        errors.append({"title": "title cannot be blank"}) if not name else None

        if not errors:
            return True
        else:
            raise ValueError(errors)

    @classmethod
    def find_by_id(cls, category_id):
        results = Category.query.filter(Category.category_id == category_id).all()
        return results[0] if results.__len__() > 0 else None

