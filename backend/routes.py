from flask import Blueprint
from root_app import app

routes = [
    {"view": app, "url_prefix": "/"},
]


def register_routes(app):
    # routing js/css/img
    for file_format in ['js', 'css', 'img']:
        blueprint = Blueprint(
            file_format, __name__,
            static_url_path="/{0}".format(file_format),
            static_folder="./static/{0}".format(file_format)
        )
        app.register_blueprint(blueprint)

    # routing other
    for route in routes:
        app.register_blueprint(route['view'], url_prefix=route['url_prefix'])
