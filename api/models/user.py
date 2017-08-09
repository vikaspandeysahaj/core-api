import uuid
from json import dumps
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from api.db_storage import storage
from api.helper.db_helper import insert, update
from api.models.role import Role
from api.models.shop import Shop


class User(storage.sql_db.Model):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(100))
    name = Column(String(200))
    mobile = Column(Integer)
    email= Column(String(200))
    about= Column(String(500))
    profile_image_url= Column(String(1000))
    profile_banner_url= Column(String(1000))
    geo_location= Column(String(200))
    fk_role_id= Column(String(100), ForeignKey('role.role_id'))
    role = relationship("Role")

    def __init__(self,
                 user_id,
                 name=None,
                 mobile=None,
                 email=None,
                 about=None,
                 profile_image_url=None,
                 profile_banner_url=None,
                 role=None,
                 geo_location=None):

        self.user_id = user_id
        self.name = name
        self.mobile = mobile
        self.email =email
        self.about=about
        self.profile_image_url = profile_image_url
        self.profile_banner_url = profile_banner_url
        self.role = role
        self.geo_location =geo_location

    def as_json(self):
        property_hash = {
            'user_id':self.user_id,
            'name': self.name,
            'mobile': self.mobile,
            'email': self.email,
            'about': self.about,
            'profile_image_url': self.profile_image_url,
            'profile_banner_url': self.profile_banner_url,
            'role': self.role.as_json(),
            'geo_location': self.geo_location,
        }
        return property_hash

    @classmethod
    def create_user(cls, user_hash=None):
        role = Role.find_by_title(Role.USER)
        user = User(user_id= uuid.uuid1().hex,
                    name=user_hash["name"],
                    mobile=user_hash["mobile"],
                    email=user_hash["email"],
                    about=user_hash["about"],
                    profile_image_url=user_hash["profile_image_url"],
                    profile_banner_url=user_hash["profile_banner_url"],
                    role=role,
                    geo_location=user_hash['geo_location'])
        insert(user)
        created_user = User.query.filter(User.user_id == user.user_id).all()
        return created_user[0] if created_user is not None else None

    def update_profile(self, user_hash):
        update(User, User.user_id == self.user_id, user_hash)
        user = User.query.filter(User.user_id == self.user_id).all()
        return user[0] if user else None

    @staticmethod
    def is_valid_hash_for_create(user_hash):
        errors = []
        name = user_hash['name']
        errors.append({"name": "name cannot be blank"}) if not name else None

        mobile = user_hash['mobile']
        errors.append({"mobile": "mobile cannot be blank"}) if not mobile else None

        if mobile.__len__()!=10:
            errors.append({"mobile": "invalid mobile number"})

        already_has = User.find_by_mobile(mobile)
        if already_has:
             errors.append({"mobile": "already exist in system"})

        if not errors:
            return True
        else:
            raise ValueError(errors)

    @classmethod
    def find_by_id(cls, user_id):
        results = User.query.filter(User.user_id == user_id).all()
        return results[0] if results.__len__() > 0 else None

    @classmethod
    def find_by_mobile(cls, mobile_number):
        results = User.query.filter(User.mobile == mobile_number).all()
        return results[0] if results.__len__() > 0 else None

    @classmethod
    def find_by_email(cls, email):
        results = User.query.filter(User.email == email).all()
        return results[0] if results.__len__() > 0 else None

    def get_home_page_for_user(self):
        home = {
            'banners': [],
            'shops': dumps([shop.as_json() for shop in Shop.find_shops_by_user(user=self)]) ,
            'offers': [],
            'recommended': [],
            'recent_view': [],
        }
        return home