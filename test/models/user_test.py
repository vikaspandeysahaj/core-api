import os
import sys
import uuid

from test.support.factories.user_factory import create_user

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/../../")

from api.models.user import User
from test.test_helper import UnitTest


class UserTest(UnitTest):
    def setUp(self):
        super(UserTest, self).setUp()
        self.user = create_user()

    def tearDown(self):
        super(UserTest, self).tearDown()

    def test_should_return_user_by_find_by_user_id(self):
        user = User.find_by_id(self.user.user_id)
        self.assertEqual(self.user, user)

    def test_should_return_None_by_find_by_user_id(self):
        user = User.find_by_id("some_wrong_user_id")
        self.assertEqual(None, user)