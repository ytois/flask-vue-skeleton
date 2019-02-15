import os
import sys

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_request_params import bind_request_params
from flask_webpack import Webpack

import models  # noqa
from models import User
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

        app.before_request(bind_request_params)

        return app

    @classmethod
    def _load_config(self, app):
        # load configure
        app.config.from_object('config.default')

        if os.getenv('FLASK_ENV', 'development') == 'production':
            app.config.from_object('config.production')
        else:
            app.config.from_object('config.development')

        app.config.from_object('config.secrets')

    @classmethod
    def _register_path(self, app):
        for path in ['utils']:
            sys.path.append(
                os.path.join(app.root_path, path)
            )


app = App.create()

# TODO: fix
login_manager = LoginManager()
login_manager.login_view = "root.LoginView:login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


if __name__ == '__main__':
    app.run()
