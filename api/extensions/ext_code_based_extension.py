from core.extension.extension import Extension
from dify_app import Flask


def init_app(app: Flask):
    code_based_extension.init()


code_based_extension = Extension()
