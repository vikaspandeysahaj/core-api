from sqlalchemy import *

meta = MetaData()

def upgrade(migrate_engine):
   meta.bind = migrate_engine
   meta.create_all()

def downgrade(migrate_engine):
   meta.bind = migrate_engine
   meta.drop_all()

users = Table(
   'user', meta,
   Column('id', Integer, primary_key=True),
   Column('user_id', String(100), unique=True),
   Column('name', String(200)),
   Column('mobile', String(130), unique=True),
   Column('email', String(200), unique=True),
   Column('about', String(500)),
   Column('profile_image_url', String(1000)),
   Column('profile_banner_url', String(1000)),
   Column('geo_location', String(200)),
   Column('fk_role_id', String(100), ForeignKey('role.role_id'))
)

roles = Table(
   'role', meta,
   Column('id', Integer, primary_key=True),
   Column('role_id', String(100), unique=True),
   Column('title', String(100), unique=True)
)

shops = Table(
   'shop', meta,
    Column('id', Integer, primary_key=True),
    Column('shop_id', String(100), unique=True),
    Column('name', String(200)),
    Column('phone', Integer),
    Column('address', String(200)),
    Column('web_site', String(100)),
    Column('shop_profile_banner_url', String(1000)),
    Column('shop_profile_image_url', String(1000)),
    Column('geo_location', String(200)),
    Column('fk_user_id', String(100), ForeignKey('user.user_id'))
)

categories = Table(
   'category', meta,
   Column('id', Integer, primary_key=True),
   Column('category_id', String(100), unique=True),
   Column('title', String(100))
)

shop_category_mapping = Table(
   'shop_category_mapping', meta,
   Column('id', Integer, primary_key=True),
   Column('fk_category_id', String(100), ForeignKey('category.category_id')),
   Column('fk_shop_id', String(100), ForeignKey('shop.shop_id'))
)

offers = Table(
   'offer', meta,
   Column('id', Integer, primary_key=True),
   Column('offer_id', String(100), unique=True),
   Column('title', String(200)),
   Column('discount', Float),
   Column('address', String(200)),
   Column('description', String(500)),
   Column('starting_time', DateTime),
   Column('end_time', DateTime),
   Column('offer_profile_banner_url', String(1000)),
   Column('geo_location', String(200)),
   Column('fk_shop_id', String(100)),
   Column('fk_category_id', String(100)),
)