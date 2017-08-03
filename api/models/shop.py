import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db_storage import storage
from api.helper.db_helper import insert
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
                 user = None):

        self.shop_id = shop_id
        self.name = name
        self.phone = phone
        self.address =address
        self.web_site=web_site
        self.shop_profile_banner_url = shop_profile_banner_url
        self.shop_profile_image_url = shop_profile_image_url
        self.user = user
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
            'user': self.user.as_json(),
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
                    user=shop_hash["user"],
                    geo_location=shop_hash['geo_location'])
        insert(shop)
        created_shop = Shop.query.filter(Shop.shop_id == shop.shop_id).all()
        return created_shop[0] if created_shop is not None else None

    @classmethod
    def find_by_id(cls, shop_id):
        results = Shop.query.filter(Shop.shop_id == shop_id).all()
        return results[0] if results.__len__() > 0 else None

    def assign_category(self, category):
        return ShopCategoryMapping.create_category(category=category,shop=self)
