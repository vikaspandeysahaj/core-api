import uuid

import datetime

from api.models.offer import Offer
from test.support.factories.category_factory import create_category
from test.support.factories.shop_factory import create_shop


def create_offer(offer_hash=None, fk_shop_id=None, fk_category_id=None):
    if offer_hash is None:
        offer_hash = {
                        'title': 'some Titile',
                        'discount': 50.5,
                        'address': "some address",
                        'description': "wow it came now!!!",
                        'offer_profile_banner_url': "some_url_location",
                        'starting_time': datetime.datetime.now(),
                        'end_time': datetime.datetime.now(),
                        'fk_shop_id': create_shop().shop_id if not fk_shop_id else fk_shop_id,
                        'fk_category_id': create_category().category_id if not fk_category_id else fk_category_id,
                        'geo_location': 'somelocation'
                    }
    return Offer.create_offer(offer_hash)

