
from flask import json

from test.support.factories.role_factory import create_role
from test.support.factories.user_factory import create_user
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
        json_user = json.loads(user_response.data)
        self.assertEqual(user_json['name'], json_user['name'])
        self.assertEqual(user_json['email'], json_user['email'])
        self.assertEqual(user_json['mobile'], json_user['mobile'])
        self.assertEqual(user_json['about'], json_user['about'])
        self.assertEqual(user_json['geo_location'], json_user['geo_location'])

    def test_get_user_api(self):
        user_json = self.get_user_json()
        user = create_user(user_json)
        uri = "/user/{user_id}".format(user_id=user.user_id)
        user_response = self.app.get(uri)
        self.assertEqual(200, user_response.status_code)
        json_user = json.loads(user_response.data)
        self.assertEqual(user_json['name'], json_user['name'])
        self.assertEqual(user_json['email'], json_user['email'])
        self.assertEqual(user_json['mobile'], json_user['mobile'])
        self.assertEqual(user_json['about'], json_user['about'])
        self.assertEqual(user_json['geo_location'], json_user['geo_location'])

    def test_user_update_api(self):
        user_json = self.get_user_json()
        user = create_user(user_json)

        user_json['name'] = 'changed_name'
        user_json['email'] = 'changed_email@gmail.com'
        user_json['mobile'] = '898989898899'

        uri = "/user/{user_id}/update".format(user_id=user.user_id)
        user_response = self.app.post(
            uri,
            data=json.dumps(user_json),
            content_type="application/json",
        )
        self.assertEqual(200, user_response.status_code)
        json_user = json.loads(user_response.data)
        self.assertEqual('changed_name', json_user['name'])
        self.assertEqual('changed_email@gmail.com', json_user['email'])
        self.assertEqual('898989898899', json_user['mobile'])
        self.assertEqual(user_json['about'], json_user['about'])
        self.assertEqual(user_json['geo_location'], json_user['geo_location'])