import uuid
from api.models.shop import Shop
from test.support.factories.category_factory import create_category
from test.support.factories.user_factory import create_user


def create_shop(shop_hash=None, user=None, category=None):
    if shop_hash is None:
        shop_hash = {
                        'name': 'myshop',
                        'phone': '123456789',
                        'address': 'some where in india',
                        'web_site': 'http://www.some_where_in_internet.com',
                        'shop_profile_banner_url': 'some_url',
                        'shop_profile_image_url': 'some_url',
                        'user': create_user() if not user else user,
                        'geo_location': 'some_where_in_map',
                        'category': create_category().as_json() if not category else category
                    }
    return Shop.create_shop(shop_hash)

