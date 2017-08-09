import traceback
from json import dumps
from flask import Blueprint, request, g

from api.decorators.permission import authenticate
from api.helper.shop_helper import get_shop_json_attr_from_hash
from api.models.shop import Shop

shop_routes = Blueprint("shop", "shop", static_folder='static')


@shop_routes.route('/shop', methods=['GET'])
@authenticate
def list_shop_api():
    try:
        shops = Shop.find_shops_by_user(g.current_user)
        return dumps([shop.as_json() for shop in shops]), 200
    except ValueError as e:
        return dumps(e.message), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400


@shop_routes.route('/shop/create', methods=['POST'])
@authenticate
def create_shop_api():
    try:
        shop_hash = get_shop_json_attr_from_hash(request.json)
        if Shop.is_valid_hash_for_create(shop_hash):
            shop_hash['fk_user_id'] = g.current_user.user_id
            shop = Shop.create_shop(shop_hash)
            return dumps(shop.as_json()), 200
    except ValueError as e:
        return dumps(e.message), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400


@shop_routes.route('/shop/<shop_id>', methods=['GET'])
@authenticate
def get_shop(shop_id):
    try:
        shop = Shop.find_by_id(shop_id)
        if shop:
            return dumps(shop.as_json()), 200
        else:
            return dumps({"Error":"Shop Not found"}), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400


@shop_routes.route('/shop/<shop_id>/update', methods=['POST'])
@authenticate
def update_shop(shop_id):
    try:
        shop_hash = get_shop_json_attr_from_hash(request.json)
        shop = Shop.find_by_id(shop_id)
        if shop:
            shop = shop.update_shop_details(shop_hash)
            return dumps(shop.as_json()), 200
        else:
            return dumps({"Error":"Shop Not found"}), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400

