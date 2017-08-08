import traceback
from json import dumps
from flask import Blueprint, request, g

from api.decorators.permission import authenticate
from api.helper.offer_helper import get_offer_json_attr_from_hash
from api.models.offer import Offer
from api.models.shop import Shop

offer_routes = Blueprint("offer", "offer", static_folder='static')


@offer_routes.route('/shop/<shop_id>/offer/create', methods=['POST'])
@authenticate
def create_offer_api(shop_id):
    try:
        offer_hash = get_offer_json_attr_from_hash(request.json)
        if Offer.is_valid_hash_for_create(offer_hash):
            offer_hash['shop'] = Shop.find_by_id(shop_id)
            offer = Offer.create_offer(offer_hash)
            return dumps(offer.as_json()), 200
    except ValueError as e:
        return dumps(e.message), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400



@offer_routes.route('/offer', methods=['POST'])
@authenticate
def list_offer_api():
    try:
        offers = Offer.find_offers_by_user(g.current_user)
        return dumps([offer.as_json() for offer in offers]), 200
    except ValueError as e:
        return dumps(e.message), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400



@offer_routes.route('/offer/<offer_id>', methods=['GET'])
@authenticate
def get_offer(offer_id):
    try:
        offer = Offer.find_by_id(offer_id)
        if offer:
            return dumps(offer.as_json()), 200
        else:
            return dumps({"Error":"Offer Not found"}), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400


@offer_routes.route('/offer/<offer_id>/update', methods=['POST'])
@authenticate
def update_offer(offer_id):
    try:
        offer_hash = get_offer_json_attr_from_hash(request.json)
        offer = Offer.find_by_id(offer_id)
        if offer:
            offer = offer.update_offer_details(offer_hash)
            return dumps(offer.as_json()), 200
        else:
            return dumps({"Error":"Offer Not found"}), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400

