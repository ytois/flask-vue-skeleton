from flask import flash, redirect, render_template, request, abort
from flask_classy import FlaskView
from sqlalchemy.orm.exc import NoResultFound

from models import User
from models.database import db
from services.google_oauth import GoogleOauthService


class InviteView(FlaskView):
    route_prefix = '/invite'

    def index(self):
        return render_template('invite_index.jade')

    def new(self):
        return render_template('invite_new.jade')

    def post(self):
        user = User.create_invite(**self._new_invite_params)
        db.session.add(user)
        db.session.commit()
        flash('create invite!')
        return redirect('root.InviteView:index')

    def get(self, code):
        try:
            user = User.query.filter(User.invite_code == code).one()
            return ''
        except NoResultFound:
            abort(404)

    @property
    def _new_invite_params(self):
        return request.params.permit('name', 'email')
