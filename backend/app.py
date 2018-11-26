from flask import Flask, Blueprint, render_template
from flask_webpack import Webpack


webpack = Webpack()


def create_app(settings_override=None):
    app = Flask(__name__)

    params = {
        'DEBUG': True,
        'WEBPACK_MANIFEST_PATH': './static/manifest.json',
    }

    app.config.update(params)

    if settings_override:
        app.config.update(settings_override)

    blueprint_js = Blueprint("javascript", __name__,
                             static_url_path='/js', static_folder='./static/js')
    blueprint_css = Blueprint(
        "css", __name__, static_url_path='/css', static_folder='./static/css')

    app.register_blueprint(blueprint_js)
    app.register_blueprint(blueprint_css)

    webpack.init_app(app)

    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')
    # return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
