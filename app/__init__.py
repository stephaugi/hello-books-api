from flask import Flask
# from .routes.hello_world_routes import hello_world_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints here

    return app