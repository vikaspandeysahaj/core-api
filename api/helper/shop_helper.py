def get_shop_json_attr_from_hash(shop_hash):
    return {
            'name': shop_hash.get("name"),
            'phone': shop_hash.get("phone"),
            'address': shop_hash.get("address"),
            'web_site': shop_hash.get("web_site"),
            'shop_profile_banner_url': shop_hash.get("shop_profile_banner_url"),
            'shop_profile_image_url': shop_hash.get("shop_profile_image_url"),
            'geo_location': shop_hash.get("geo_location"),
            'category': shop_hash.get("category")

    }
