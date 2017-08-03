import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from api.db_storage import storage
from api.helper.db_helper import insert


class Offer(storage.sql_db.Model):

    __tabletitle__ = 'offer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    offer_id = Column(String(100))
    title = Column(String(200))
    discount = Column(Float)
    address= Column(String(200))
    description= Column(String(500))
    starting_time= Column(DateTime)
    end_time= Column(DateTime)
    offer_profile_banner_url= Column(String(1000))
    geo_location= Column(String(200))
    fk_shop_id= Column(String(100), ForeignKey('shop.shop_id'))
    fk_category_id= Column(String(100), ForeignKey('category.category_id'))
    shop = relationship("Shop")
    category = relationship("Category")

    def __init__(self,
                 offer_id = None,
                 title = None,
                 discount = None,
                 address= None,
                 description= None,
                 offer_profile_banner_url= None,
                 geo_location= None,
                 shop = None,
                 category=None,
                 starting_time=None,
                 end_time=None):

        self.offer_id = offer_id
        self.title = title
        self.discount = discount
        self.address =address
        self.description=description
        self.offer_profile_banner_url = offer_profile_banner_url
        self.shop = shop
        self.category = category
        self.starting_time= starting_time
        self.end_time = end_time
        self.geo_location =geo_location

    def as_json(self):
        property_hash = {
            'offer_id':self.offer_id,
            'title': self.title,
            'discount': self.discount,
            'address': self.address,
            'description': self.description,
            'offer_profile_banner_url': self.offer_profile_banner_url,
            'starting_time': self.starting_time,
            'end_time': self.end_time,
            'shop': self.shop.as_json(),
            'geo_location': self.geo_location,
        }
        return property_hash

    @classmethod
    def create_offer(cls, offer_hash=None):
        offer = Offer(offer_id= uuid.uuid1().hex,
                    title=offer_hash["title"],
                    discount=offer_hash["discount"],
                    address=offer_hash["address"],
                    description=offer_hash["description"],
                    starting_time=offer_hash["starting_time"],
                    end_time=offer_hash["end_time"],
                    category=offer_hash["category"],
                    offer_profile_banner_url=offer_hash["offer_profile_banner_url"],
                    shop=offer_hash["shop"],
                    geo_location=offer_hash['geo_location'])
        insert(offer)
        created_offer = Offer.query.filter(Offer.offer_id == offer.offer_id).all()
        return created_offer[0] if created_offer is not None else None

    @classmethod
    def find_by_id(cls, offer_id):
        results = Offer.query.filter(Offer.offer_id == offer_id).all()
        return results[0] if results.__len__() > 0 else None

    @classmethod
    def find_by_shop(cls, shop):
        results = Offer.query.filter(Offer.shop == shop).all()
        return results if results.__len__() > 0 else None

    @classmethod
    def find_by_category(cls, category):
        results = Offer.query.filter(Offer.category == category).all()
        return results if results.__len__() > 0 else None
