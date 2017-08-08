import os
import sys

from test.support.factories.category_factory import create_category
from test.support.factories.offer_factory import create_offer
from test.support.factories.role_factory import create_role
from test.support.factories.shop_factory import create_shop
from test.support.factories.user_factory import create_user

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/../../")

from api.models.offer import Offer
from test.test_helper import UnitTest


class OfferTest(UnitTest):
    def setUp(self):
        super(OfferTest, self).setUp()
        self.category1 = create_category(title='electronics')
        self.category2 = create_category(title='food')

        shop_1_hash = {
                'name': 'myshop1',
                'fk_user_id': create_user(mobile='123456789', email="test@test.com").user_id,
                'phone': '123456789',
                'address': 'some where in india',
                'web_site': 'http://www.some_where_in_internet.com',
                'shop_profile_banner_url': 'some_url',
                'shop_profile_image_url': 'some_url',
                'geo_location': 'some_where_in_map',
                'fk_category_id': create_category().category_id
            }
        self.shop1 = create_shop(shop_hash=shop_1_hash)
        self.offer = create_offer(fk_category_id=self.category1.category_id, fk_shop_id=self.shop1.shop_id)
        self.offer = create_offer(fk_category_id=self.category2.category_id, fk_shop_id=self.shop1.shop_id)


    def tearDown(self):
        super(OfferTest, self).tearDown()

    def test_should_return_offer_by_find_by_offer_id(self):
        offer = Offer.find_by_id(self.offer.offer_id)
        self.assertEqual(self.offer, offer)

    def test_should_return_None_by_find_by_offer_id(self):
        offer = Offer.find_by_id("some_wrong_offer_id")
        self.assertEqual(None, offer)

    def test_should_return_offer_by_category(self):
        offer = Offer.find_by_category(self.category1)
        self.assertEqual(self.category1, offer[0].category)

    def test_should_return_offer_by_shop(self):
        offer = Offer.find_by_shop(self.shop1)
        self.assertEqual(self.shop1, offer[0].shop)