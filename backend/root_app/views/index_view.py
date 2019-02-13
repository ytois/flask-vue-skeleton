from flask import render_template
from flask_classy import FlaskView


class IndexView(FlaskView):
    def index(self):
        return render_template('index.jade')
