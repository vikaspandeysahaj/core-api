import os
import sys

from test.support.factories.shop_factory import create_shop

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/../../")

from api.models.shop import Shop
from test.test_helper import UnitTest


class ShopTest(UnitTest):
    def setUp(self):
        super(ShopTest, self).setUp()
        self.shop = create_shop()

    def tearDown(self):
        super(ShopTest, self).tearDown()

    def test_should_return_shop_by_find_by_shop_id(self):
        shop = Shop.find_by_id(self.shop.shop_id)
        self.assertEqual(self.shop, shop)

    def test_should_return_None_by_find_by_shop_id(self):
        shop = Shop.find_by_id("some_wrong_shop_id")
        self.assertEqual(None, shop)