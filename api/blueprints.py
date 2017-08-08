from api.controllers.offer_controller import offer_routes
from api.controllers.shop_controller import shop_routes
from api.controllers.user_controller import user_routes

def register_blueprints(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(shop_routes)
    app.register_blueprint(offer_routes)

