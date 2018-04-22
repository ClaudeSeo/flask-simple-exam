from flask import Flask
from app.views.anime import bp as anime_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(anime_bp)
    app.config.from_object('app.config')
    return app
