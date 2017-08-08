import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db_storage import storage
from api.helper.db_helper import insert, update
from api.models.category import Category
from api.models.shop_category_mapping import ShopCategoryMapping


class Shop(storage.sql_db.Model):

    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True, autoincrement=True)
    shop_id = Column(String(100))
    name = Column(String(200))
    phone = Column(Integer)
    address= Column(String(200))
    web_site= Column(String(500))
    shop_profile_banner_url= Column(String(1000))
    shop_profile_image_url= Column(String(1000))
    geo_location= Column(String(200))
    fk_user_id= Column(String(100), ForeignKey('user.user_id'))
    user = relationship("User")

    def __init__(self,
                 shop_id = None,
                 name = None,
                 phone = None,
                 address= None,
                 web_site= None,
                 shop_profile_banner_url= None,
                 shop_profile_image_url= None,
                 geo_location= None,
                 fk_user_id = None):

        self.shop_id = shop_id
        self.name = name
        self.phone = phone
        self.address =address
        self.web_site=web_site
        self.shop_profile_banner_url = shop_profile_banner_url
        self.shop_profile_image_url = shop_profile_image_url
        self.fk_user_id = fk_user_id
        self.geo_location =geo_location

    def as_json(self):
        property_hash = {
            'shop_id':self.shop_id,
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'web_site': self.web_site,
            'shop_profile_banner_url': self.shop_profile_banner_url,
            'shop_profile_image_url': self.shop_profile_image_url,
            # 'user': self.user.as_json(),
            'geo_location': self.geo_location,
        }
        return property_hash

    @classmethod
    def create_shop(cls, shop_hash=None):
        shop = Shop(shop_id= uuid.uuid1().hex,
                    name=shop_hash["name"],
                    phone=shop_hash["phone"],
                    address=shop_hash["address"],
                    web_site=shop_hash["web_site"],
                    shop_profile_banner_url=shop_hash["shop_profile_banner_url"],
                    shop_profile_image_url=shop_hash["shop_profile_image_url"],
                    fk_user_id=shop_hash['fk_user_id'],
                    geo_location=shop_hash['geo_location'])
        insert(shop)
        category = Category.query.filter(Category.category_id == shop_hash['fk_category_id']).all()[0]
        created_shop = Shop.query.filter(Shop.shop_id == shop.shop_id).all()
        created_shop[0].assign_category(category=category)
        return created_shop[0] if created_shop is not None else None

    def update_shop_details(self, shop_hash):
        del shop_hash['fk_category_id']
        update(Shop, Shop.shop_id == self.shop_id, shop_hash)
        shop = Shop.query.filter(Shop.shop_id == self.shop_id).all()
        return shop[0] if shop else None

    @staticmethod
    def is_valid_hash_for_create(shop_hash):
        errors = []
        name = shop_hash['name']
        errors.append({"name": "name cannot be blank"}) if not name else None

        mobile = shop_hash['geo_location']
        errors.append({"geo_location": "geo_location cannot be blank"}) if not mobile else None

        category = shop_hash['fk_category_id']
        errors.append({"category": "category cannot be blank"}) if not category else None


        if not errors:
            return True
        else:
            raise ValueError(errors)

    @classmethod
    def find_by_id(cls, shop_id):
        results = Shop.query.filter(Shop.shop_id == shop_id).all()
        return results[0] if results.__len__() > 0 else None

    def assign_category(self, category):
        return ShopCategoryMapping.create_category(category=category,shop=self)

    @classmethod
    def find_shops_by_user(cls, user):
        results = Shop.query.filter(Shop.fk_user_id == user.user_id).all()
        return results