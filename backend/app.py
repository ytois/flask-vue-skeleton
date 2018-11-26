from flask import Flask, Blueprint, render_template
from flask_webpack import Webpack


def create_app(settings_override=None):
    app = Flask(__name__)

    params = {
        'DEBUG': True,
        'WEBPACK_MANIFEST_PATH': './static/manifest.json',
    }

    app.config.update(params)

    if settings_override:
        app.config.update(settings_override)

    # use template pug(jade)
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    # routing js/css
    blueprint_js = Blueprint(
        "javascript",
        __name__,
        static_url_path='/js',
        static_folder='./static/js'
    )
    blueprint_css = Blueprint(
        "css",
        __name__,
        static_url_path='/css',
        static_folder='./static/css'
    )

    app.register_blueprint(blueprint_js)
    app.register_blueprint(blueprint_css)

    # use webpack
    webpack = Webpack()
    webpack.init_app(app)

    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.jade')


if __name__ == '__main__':
    app.run()
