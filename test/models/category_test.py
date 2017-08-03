import os
import sys
import uuid

from test.support.factories.category_factory import create_category

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/../../")

from api.models.category import Category
from test.test_helper import UnitTest


class CategoryTest(UnitTest):
    def setUp(self):
        super(CategoryTest, self).setUp()
        self.category = create_category()

    def tearDown(self):
        super(CategoryTest, self).tearDown()

    def test_should_return_category_by_find_by_category_id(self):
        category = Category.find_by_id(self.category.category_id)
        self.assertEqual(self.category, category)

    def test_should_return_None_by_find_by_category_id(self):
        category = Category.find_by_id("some_wrong_category_id")
        self.assertEqual(None, category)