from dify_app import Flask


def init_app(app: Flask):
    import flask_migrate  # type: ignore

    from extensions.ext_database import db

    flask_migrate.Migrate(app, db)
