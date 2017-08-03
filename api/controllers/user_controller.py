import traceback
from json import dumps
from flask import Blueprint, request

from api.helper.user_helper import get_user_json_attr_from_hash
from api.models.user import User

user_routes = Blueprint("user", "user", static_folder='static')

@user_routes.route('/user/create', methods=['POST'])
def create_user():
    try:
        user_hash = get_user_json_attr_from_hash(request.json)
        if User.is_valid_hash_for_create(user_hash):
            user = User.create_user(user_hash)
            return dumps(user.as_json()), 200
    except ValueError as e:
        return dumps(e.message), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400


@user_routes.route('/user/<user_id>', methods=['GET'])
def get_profile(user_id):
    try:
        user = User.find_by_id(user_id)
        if user:
            return dumps(user.as_json()), 200
        else:
            return dumps({"Error":"User Not found"}), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400

@user_routes.route('/user/<user_id>/update', methods=['POST'])
def update_profile(user_id):
    try:
        user_hash = get_user_json_attr_from_hash(request.json)
        user = User.find_by_id(user_id)
        if user:
            user = user.update_profile(user_hash)
            return dumps(user.as_json()), 200
        else:
            return dumps({"Error":"User Not found"}), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400
