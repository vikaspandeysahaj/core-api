import os
import sys
import uuid

from test.support.factories.role_factory import create_role

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + "/../../")

from api.models.role import Role
from test.test_helper import UnitTest


class RoleTest(UnitTest):
    def setUp(self):
        super(RoleTest, self).setUp()
        self.role = create_role()

    def tearDown(self):
        super(RoleTest, self).tearDown()

    def test_should_return_role_by_find_by_role_id(self):
        role = Role.find_by_id(self.role.role_id)
        self.assertEqual(self.role, role)

    def test_should_return_None_by_find_by_role_id(self):
        role = Role.find_by_id("some_wrong_role_id")
        self.assertEqual(None, role)