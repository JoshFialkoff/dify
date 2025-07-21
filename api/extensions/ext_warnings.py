from dify_app import Flask


def init_app(app: Flask):
    import warnings

    warnings.simplefilter("ignore", ResourceWarning)
