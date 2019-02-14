import os
import sys

from flask import Flask
from flask_webpack import Webpack
from flask_debugtoolbar import DebugToolbarExtension

import models  # noqa
from models.database import init_db
from routes import register_routes


class App:
    @classmethod
    def create(self):
        return self._create_app()

    @classmethod
    def _create_app(self):
        app = Flask(__name__)

        self._load_config(app)
        self._register_path(app)

        # use template pug(jade)
        app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

        # use webpack
        webpack = Webpack()
        webpack.init_app(app)

        # routing
        register_routes(app)

        # init db
        init_db(app)

        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

        return app

    @classmethod
    def _load_config(self, app):
        # load configure
        app.config.from_object('config.default')

        if os.getenv('FLASK_ENV', 'development') == 'production':
            app.config.from_object('config.production')
        else:
            app.config.from_object('config.development')

        app.config.from_pyfile('secrets.py', silent=True)

    @classmethod
    def _register_path(self, app):
        for path in ['utils']:
            sys.path.append(
                os.path.join(app.root_path, path)
            )


app = App.create()


if __name__ == '__main__':
    app.run()
