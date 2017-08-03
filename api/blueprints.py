from api.controllers.user_controller import user_routes

def register_blueprints(app):
    app.register_blueprint(user_routes)

