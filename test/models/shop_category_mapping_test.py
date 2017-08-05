import os
import sys
import uuid

from api.models.shop_category_mapping import ShopCategoryMapping
from test.support.factories.category_factory import create_category
from test.support.factories.role_factory import create_role
from test.support.factories.shop_factory import create_shop
from test.support.factories.user_factory import create_user

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/../../")

from test.test_helper import UnitTest


class CategoryTest(UnitTest):
    def setUp(self):
        super(CategoryTest, self).setUp()
        self.category = create_category(title='other')
        self.category1 = create_category(title='electronics')
        self.category2 = create_category(title='food')
        shop_1_hash = {
                'name': 'myshop1',
                'user': create_user(mobile='123456789', email="test@test.com"),
                'phone': '123456789',
                'address': 'some where in india',
                'web_site': 'http://www.some_where_in_internet.com',
                'shop_profile_banner_url': 'some_url',
                'shop_profile_image_url': 'some_url',
                'geo_location': 'some_where_in_map',
                'category': self.category.as_json()
            }
        shop_2_hash = {
                'name': 'myshop',
                'user': create_user(mobile='987654321', email="test2@test.com"),
                'phone': '123456789',
                'address': 'some where in india',
                'web_site': 'http://www.some_where_in_internet.com',
                'shop_profile_banner_url': 'some_url',
                'shop_profile_image_url': 'some_url',
                'geo_location': 'some_where_in_map',
                'category': self.category.as_json()
            }
        self.shop1 = create_shop(shop_hash=shop_1_hash)
        self.shop2 = create_shop(shop_hash=shop_2_hash)


    def tearDown(self):
        super(CategoryTest, self).tearDown()

    def test_should_return_category_mapping_by_find_by_category_id(self):
        self.shop1.assign_category(self.category1)
        self.shop1.assign_category(self.category2)
        self.shop2.assign_category(self.category1)
        self.shop2.assign_category(self.category2)
        category_mapping = ShopCategoryMapping.find_by_category_id(self.category1.category_id)
        self.assertEquals(len(category_mapping), 2)

    def test_should_return_category_mapping_by_find_by_shop_id(self):
        self.shop1.assign_category(self.category1)
        self.shop1.assign_category(self.category2)
        self.shop2.assign_category(self.category1)
        category_mapping = ShopCategoryMapping.find_by_shop_id(self.shop1.shop_id)
        self.assertEquals(len(category_mapping), 3)
        category_mapping = ShopCategoryMapping.find_by_shop_id(self.shop2.shop_id)
        self.assertEquals(len(category_mapping), 2)