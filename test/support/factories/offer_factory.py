import uuid

import datetime

from api.models.offer import Offer
from test.support.factories.category_factory import create_category
from test.support.factories.shop_factory import create_shop


def create_offer(offer_hash=None, shop=None, category=None):
    if offer_hash is None:
        offer_hash = {
                        'title': 'some Titile',
                        'discount': 50.5,
                        'address': "some address",
                        'description': "wow it came now!!!",
                        'offer_profile_banner_url': "some_url_location",
                        'starting_time': datetime.datetime.now(),
                        'end_time': datetime.datetime.now(),
                        'shop': create_shop() if not shop else shop,
                        'category': create_category() if not category else category,
                        'geo_location': 'somelocation'
                    }
    return Offer.create_offer(offer_hash)

