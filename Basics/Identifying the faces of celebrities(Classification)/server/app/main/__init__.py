from flask import Flask
from app.main.config import config_by_name
from flask_cors import CORS
fromapp.main.config import photos
from flask_uploads import configure_uploads

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    configure_uploads(app, photos)
    CORS(app)
    return app