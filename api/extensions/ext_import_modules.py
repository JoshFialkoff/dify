from dify_app import Flask


def init_app(app: Flask):
    from events import event_handlers  # noqa: F401
