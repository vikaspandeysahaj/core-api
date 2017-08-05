
from flask import json

from test.support.factories.category_factory import create_category
from test.support.factories.role_factory import create_role
from test.support.factories.shop_factory import create_shop
from test.support.factories.user_factory import create_user
from test.test_helper import ServiceTest


class ShopControllerTest(ServiceTest):
    def setUp(self):
        super(ShopControllerTest, self).setUp()
        create_role('user')
        create_role('admin')
        create_role('shop')
        self.user = create_user()
        self.category = create_category()


    def tearDown(self):
        super(ShopControllerTest, self).tearDown()

    def get_shop_json(self):
        shop_request ={
                        'name': "Shop_name",
                        'phone': 299889898,
                        'address': "Shop_address",
                        'web_site': "Shop_web_site",
                        'shop_profile_banner_url': "shop_shop_profile_banner_url",
                        'shop_profile_image_url': "shop_shop_profile_image_url",
                        'geo_location': "shop_geo_location",
                        'category': self.category.as_json()
                    }
        return shop_request

    def test_shop_registration_api(self):
        headers_dict = {'EMAIL': self.user.email}
        shop_json = self.get_shop_json()
        uri = "/shop/create"
        shop_response = self.app.post(
            uri,
            data=json.dumps(shop_json),
            content_type="application/json",
            headers=headers_dict
        )
        self.assertEqual(200, shop_response.status_code)
        json_shop = json.loads(shop_response.data)
        self.assertEqual(shop_json['name'], json_shop['name'])
        self.assertEqual(shop_json['phone'], json_shop['phone'])
        self.assertEqual(shop_json['address'], json_shop['address'])
        self.assertEqual(shop_json['web_site'], json_shop['web_site'])
        self.assertEqual(shop_json['shop_profile_banner_url'], json_shop['shop_profile_banner_url'])
        self.assertEqual(shop_json['shop_profile_image_url'], json_shop['shop_profile_image_url'])
        self.assertEqual(shop_json['geo_location'], json_shop['geo_location'])

    def test_get_shop_api(self):
        headers_dict = {'EMAIL': self.user.email}
        shop = create_shop(user=self.user, category=self.category.as_json())
        uri = "/shop/{shop_id}".format(shop_id=shop.shop_id)
        user_response = self.app.get(
            uri,
            headers=headers_dict
        )
        self.assertEqual(200, user_response.status_code)
        json_shop = json.loads(user_response.data)
        self.assertEqual(shop.name, json_shop['name'])
        self.assertEqual(shop.phone, json_shop['phone'])
        self.assertEqual(shop.address, json_shop['address'])
        self.assertEqual(shop.web_site, json_shop['web_site'])
        self.assertEqual(shop.shop_profile_banner_url, json_shop['shop_profile_banner_url'])
        self.assertEqual(shop.shop_profile_image_url, json_shop['shop_profile_image_url'])
        self.assertEqual(shop.geo_location, json_shop['geo_location'])

    def test_shop_update_api(self):
        headers_dict = {'EMAIL': self.user.email}
        shop_json = self.get_shop_json()
        shop = create_shop(shop_hash=shop_json, user=self.user, category=self.category.as_json())
        shop_json['name'] = 'changed_name'
        shop_json['phone'] = 898989889
        shop_json['address'] = 'some_address'
        shop_json['web_site'] = 'changed_web_site'
        shop_json['shop_profile_banner_url'] = 'changed_url_banner'
        shop_json['shop_profile_image_url'] = 'changed_url_profile'
        uri = "/shop/{shop_id}/update".format(shop_id=shop.shop_id)
        user_response = self.app.post(
            uri,
            data=json.dumps(shop_json),
            content_type="application/json",
            headers=headers_dict
        )
        self.assertEqual(200, user_response.status_code)
        json_user = json.loads(user_response.data)
        self.assertEqual('changed_name', json_user['name'])
        self.assertEqual('changed_web_site', json_user['web_site'])
        self.assertEqual(898989889, json_user['phone'])
        self.assertEqual(shop_json['geo_location'], json_user['geo_location'])
        self.assertEqual(shop_json['shop_profile_banner_url'], json_user['shop_profile_banner_url'])
        self.assertEqual(shop_json['shop_profile_image_url'], json_user['shop_profile_image_url'])