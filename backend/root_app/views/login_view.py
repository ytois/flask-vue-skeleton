from flask import redirect, request, url_for, flash, session
from flask_classy import FlaskView, route
from services.google_oauth import GoogleOauthService


class LoginView(FlaskView):
    route_base = '/'

    @route('/login')
    def login(self):
        url = url_for('root.LoginView:callback', _external=True)
        return GoogleOauthService().authorize(callback_url=url, next_url=None)

    @route('/callback')
    def callback(self):
        next_url = request.args.get('next') or url_for('root.index_view')
        account = GoogleOauthService().fetch_account()

        if not account.verify():
            flash('Login fail.')
            redirect(url_for('root.index_view'))

        self._save_session(account.access_token)
        return redirect(next_url)

    @route('/logout')
    def logout(self):
        self._delete_session()
        return redirect(url_for('root.index_view'))

    def _save_session(self, access_token):
        session['access_token'] = access_token

    def _delete_session(self):
        if 'access_token' in session:
            del session['access_token']
