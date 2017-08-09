import datetime
from unittest import skip

from flask import json

from test.support.factories.category_factory import create_category
from test.support.factories.role_factory import create_role
from test.support.factories.offer_factory import create_offer
from test.support.factories.shop_factory import create_shop
from test.support.factories.user_factory import create_user
from test.test_helper import ServiceTest


class OfferControllerTest(ServiceTest):
    def setUp(self):
        super(OfferControllerTest, self).setUp()
        create_role('user')
        create_role('admin')
        create_role('offer')
        self.user = create_user()
        self.category = create_category()
        self.shop = create_shop(fk_user_id=self.user.user_id, fk_category_id=self.category.category_id)

    def tearDown(self):
        super(OfferControllerTest, self).tearDown()

    def get_offer_json(self):
        offer_request ={
                        'title': "offer_title",
                        'discount': 30.7,
                        'address': "some address",
                        'description': "Some description",
                        'offer_profile_banner_url': "offer_profile_banner_url",
                        'starting_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'end_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'fk_shop_id': self.shop.shop_id,
                        'geo_location': 'geo-locarion',
                        'fk_category_id': self.category.category_id
                    }
        return offer_request

    def test_offer_registration_api(self):
        headers_dict = {'EMAIL': self.user.email}
        offer_json = self.get_offer_json()
        uri = "/shop/{shop_id}/offer/create".format(shop_id=self.shop.shop_id)
        offer_response = self.app.post(
            uri,
            data=json.dumps(offer_json),
            content_type="application/json",
            headers=headers_dict
        )
        self.assertEqual(200, offer_response.status_code)
        json_offer = json.loads(offer_response.data)
        self.assertEqual(offer_json['title'], json_offer['title'])
        self.assertEqual(offer_json['discount'], json_offer['discount'])
        self.assertEqual(offer_json['address'], json_offer['address'])
        self.assertEqual(offer_json['description'], json_offer['description'])
        self.assertEqual(offer_json['offer_profile_banner_url'], json_offer['offer_profile_banner_url'])
        self.assertEqual(offer_json['starting_time'], json_offer['starting_time'])
        self.assertEqual(offer_json['geo_location'], json_offer['geo_location'])
        self.assertEqual(offer_json['end_time'], json_offer['end_time'])

    def test_get_all_offers_for_shop_api(self):
        headers_dict = {'EMAIL': self.user.email}
        offer_1 = create_offer(fk_shop_id=self.shop.shop_id)
        offer_2 = create_offer(fk_shop_id=self.shop.shop_id)
        offer_3 = create_offer(fk_shop_id=self.shop.shop_id)
        offer_4 = create_offer(fk_shop_id=self.shop.shop_id)
        uri = "/shop/{shop_id}/offer".format(shop_id=self.shop.shop_id)
        offer_response = self.app.get(
            uri,
            headers=headers_dict
        )
        self.assertEqual(200, offer_response.status_code)
        json_offer = json.loads(offer_response.data)
        self.assertEqual(4, len(json_offer))

    def test_get_offer_api(self):
        headers_dict = {'EMAIL': self.user.email}
        offer = create_offer(fk_shop_id=self.shop.shop_id)
        uri = "/offer/{offer_id}".format(offer_id=offer.offer_id)
        user_response = self.app.get(
            uri,
            headers=headers_dict
        )
        self.assertEqual(200, user_response.status_code)
        json_shop = json.loads(user_response.data)
        self.assertEqual(offer.title, json_shop['title'])
        self.assertEqual(offer.address, json_shop['address'])

    def test_offer_update_api(self):
        headers_dict = {'EMAIL': self.user.email}
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        offer_json = self.get_offer_json()
        offer = create_offer(fk_shop_id=self.shop.shop_id)
        offer_json['title'] = 'changed_name'
        offer_json['discount'] = 89
        offer_json['address'] = 'some_address'
        offer_json['description'] = 'changed_web_site'
        offer_json['starting_time'] = date
        offer_json['end_time'] = date
        uri = "/offer/{offer_id}/update".format(offer_id=offer.offer_id)
        user_response = self.app.post(
            uri,
            data=json.dumps(offer_json),
            content_type="application/json",
            headers=headers_dict
        )
        self.assertEqual(200, user_response.status_code)
        json_offer = json.loads(user_response.data)
        self.assertEqual('changed_name', json_offer['title'])
        self.assertEqual(89, json_offer['discount'])
        self.assertEqual('some_address', json_offer['address'])
        self.assertEqual('changed_web_site', json_offer['description'])
        self.assertEqual(date[0], datetime.datetime.strptime(json_offer['starting_time'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'))
        self.assertEqual(date[0], datetime.datetime.strptime(json_offer['end_time'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'))

