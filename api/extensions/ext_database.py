from dify_app import Flask
from models import db


def init_app(app: Flask):
    db.init_app(app)
