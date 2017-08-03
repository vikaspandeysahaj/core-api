
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.db_storage import storage
from api.helper.db_helper import insert


class ShopCategoryMapping(storage.sql_db.Model):

    __tablename__ = 'shop_category_mapping'
    id = Column(Integer, primary_key=True, autoincrement=True)

    fk_shop_id= Column(String(100), ForeignKey('shop.shop_id'))
    fk_category_id= Column(String(100), ForeignKey('category.category_id'))
    shop = relationship("Shop")
    category = relationship("Category")


    def __init__(self,
                 fk_shop_id,
                 fk_category_id):

        self.fk_category_id = fk_category_id
        self.fk_shop_id = fk_shop_id

    def as_json(self):
        property_hash = {
            'category':self.category,
            'shop': self.shop
        }
        return property_hash

    @classmethod
    def create_category(cls, category, shop):
        category_mapping = ShopCategoryMapping(fk_shop_id=shop.shop_id,
                                       fk_category_id=category.category_id)
        created_category_mapping = insert(category_mapping)
        return created_category_mapping[0] if created_category_mapping is not None else None


    @classmethod
    def find_by_category_id(cls, category_id):
        results = ShopCategoryMapping.query.filter(ShopCategoryMapping.fk_category_id == category_id).all()
        return results if results.__len__() > 0 else None

    @classmethod
    def find_by_shop_id(cls, shop_id):
        results = ShopCategoryMapping.query.filter(ShopCategoryMapping.fk_shop_id == shop_id).all()
        return results if results.__len__() > 0 else None
