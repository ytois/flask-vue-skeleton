from flask import Flask, Blueprint, render_template
from flask_webpack import Webpack
import os


def create_app():
    app = Flask(__name__)

    # configure
    app.config.from_object('config.default')

    if os.getenv('FLASK_ENV', 'development') == 'production':
        app.config.from_object('config.production')
    else:
        app.config.from_object('config.development')

    app.config.from_pyfile('secrets.py', silent=True)

    # use template pug(jade)
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    # routing js/css/img
    for file_format in ['js', 'css', 'img']:
        blueprint = Blueprint(
            file_format, __name__,
            static_url_path="/{0}".format(file_format),
            static_folder="./static/{0}".format(file_format)
        )
        app.register_blueprint(blueprint)

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
