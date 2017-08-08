def get_offer_json_attr_from_hash(offer_hash):
    return {
            'title': offer_hash.get("title"),
            'discount': offer_hash.get("discount"),
            'address': offer_hash.get("address"),
            'description': offer_hash.get("description"),
            'offer_profile_banner_url': offer_hash.get("offer_profile_banner_url"),
            'starting_time': offer_hash.get("starting_time"),
            'end_time': offer_hash.get("end_time"),
            'geo_location': offer_hash.get("geo_location"),
            'fk_category_id': offer_hash.get("fk_category_id"),
            'fk_shop_id': offer_hash.get("fk_shop_id"),

    }
