from core.hosting_configuration import HostingConfiguration

hosting_configuration = HostingConfiguration()


from dify_app import Flask


def init_app(app: Flask):
    hosting_configuration.init_app(app)
