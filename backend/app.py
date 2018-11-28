from flask import Flask
from flask_webpack import Webpack
from routes import register_routes
import os


def create_app():
    app = Flask(__name__)

    # load configure
    app.config.from_object('config.default')

    if os.getenv('FLASK_ENV', 'development') == 'production':
        app.config.from_object('config.production')
    else:
        app.config.from_object('config.development')

    app.config.from_pyfile('secrets.py', silent=True)

    # use template pug(jade)
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    # use webpack
    webpack = Webpack()
    webpack.init_app(app)

    # routing
    register_routes(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
