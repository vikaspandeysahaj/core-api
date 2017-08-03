
from flask import json

from test.support.factories.role_factory import create_role
from test.test_helper import ServiceTest


class UserControllerTest(ServiceTest):
    def setUp(self):
        super(UserControllerTest, self).setUp()
        create_role('user')
        create_role('admin')
        create_role('shop')

    def tearDown(self):
        super(UserControllerTest, self).tearDown()

    def get_user_json(self):
        user_request ={
                        'name': "test_user",
                        'email':"test_user@poc.com",
                        'mobile': '1234567890',
                        'profile_image_url': "some_url",
                        'profile_banner_url': "some_url",
                        'about': 'this is about me test',
                        'geo_location':'00000,200000'
                    }
        return user_request

    def test_user_registration_api(self):
        user_json = self.get_user_json()
        uri = "/user/create"
        user_response = self.app.post(
            uri,
            data=json.dumps(user_json),
            content_type="application/json",
        )
        self.assertEqual(200, user_response.status_code)

