from flask import flash, redirect, request, url_for
from flask_classy import FlaskView, route
from flask_login import login_user, logout_user

from models import User
from services.google_oauth import GoogleOauthService


class LoginView(FlaskView):
    @route('/login')
    def login(self):
        url = url_for('root.LoginView:callback', _external=True)
        return GoogleOauthService().authorize(callback_url=url, next_url=None)

    @route('/callback')
    def callback(self):
        next_url = request.args.get('next') or url_for('root.IndexView:index')
        account = GoogleOauthService().fetch_account()

        user = User.find_by_email(account.email)

        if not account.verify_organization():
            flash('Login fail.')
            redirect('root.IndexView:index')
        elif user is None:
            flash('User not found.')
            redirect('root.IndexView:index')

        login_user(user)
        flash('Login success.')
        flash(f'Welcom {user.name}!')
        return redirect(next_url)

    @route('/logout')
    def logout(self):
        logout_user()
        flash('Logout.')
        return redirect(url_for('root.IndexView:index'))
