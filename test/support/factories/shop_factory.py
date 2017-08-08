import uuid
from api.models.shop import Shop
from test.support.factories.category_factory import create_category
from test.support.factories.user_factory import create_user


def create_shop(shop_hash=None, fk_user_id=None, fk_category_id=None):
    if shop_hash is None:
        shop_hash = {
                        'name': 'myshop',
                        'phone': '123456789',
                        'address': 'some where in india',
                        'web_site': 'http://www.some_where_in_internet.com',
                        'shop_profile_banner_url': 'some_url',
                        'shop_profile_image_url': 'some_url',
                        'fk_user_id': create_user().user_id if not fk_user_id else fk_user_id,
                        'geo_location': 'some_where_in_map',
                        'fk_category_id': create_category().category_id if not fk_category_id else fk_category_id
                    }
    return Shop.create_shop(shop_hash)

