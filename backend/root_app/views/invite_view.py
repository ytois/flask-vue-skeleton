from flask import flash, redirect, render_template, request
from flask_classy import FlaskView

from models import User
from models.database import db


class InviteView(FlaskView):
    route_prefix = '/invite'

    def new(self):
        return render_template('invite_new.jade')

    def post(self):
        email = self._new_invite_params['email']
        if User.find_by_email(email):
            flash(f'[{email}] is already exists!')
        else:
            user = User(**self._new_invite_params)
            db.session.add(user)
            db.session.commit()
            flash('create invite!')
        return redirect('root.InviteView:index')

    @property
    def _new_invite_params(self):
        return request.params.permit('name', 'email')
