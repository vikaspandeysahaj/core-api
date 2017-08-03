def get_user_json_attr_from_hash(user_hash):
    return {
            'name': user_hash.get("name"),
            'mobile': user_hash.get("mobile"),
            'email': user_hash.get("email"),
            'about': user_hash.get("about"),
            'profile_image_url': user_hash.get("profile_image_url"),
            'profile_banner_url': user_hash.get("profile_banner_url"),
            'geo_location': user_hash.get("geo_location"),
    }
