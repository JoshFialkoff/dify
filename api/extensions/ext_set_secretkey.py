from configs import dify_config
from dify_app import Flask


def init_app(app: Flask):
    app.secret_key = dify_config.SECRET_KEY
