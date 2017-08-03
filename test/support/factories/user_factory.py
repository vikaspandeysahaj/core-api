import uuid
from api.models.user import User
from test.support.factories.role_factory import create_role


def create_user(user_hash=None, mobile=None, email=None):
    if user_hash is None:
        user_hash = {
                        'name': "test_user",
                        'email':"test_user@poc.com" if not email else email,
                        'mobile': '1234567890' if not mobile else mobile,
                        'profile_image_url': "some_url",
                        'profile_banner_url': "some_url",
                        'about': 'this is about me test',
                        'geo_location':'00000,200000',
                    }
    return User.create_user(user_hash)

