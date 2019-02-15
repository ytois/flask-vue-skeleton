import requests
from flask import current_app
from flask_oauthlib.client import OAuth


class GoogleOauthService:
    def __init__(self):
        self.errors = []
        self._activate_development_mode()

    @property
    def oauth(self):
        oauth = OAuth()
        oauth.remote_app(
            'google',
            base_url='https://www.google.com/accounts/',
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            request_token_url=None,
            request_token_params={
                'scope': [
                    'https://www.googleapis.com/auth/userinfo.email',
                    'https://www.googleapis.com/auth/userinfo.profile',
                ]
            },
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_method='POST',
            consumer_key=current_app.config['GOOGLE_CLIENT_ID'],
            consumer_secret=current_app.config['GOOGLE_CLIENT_SECRET']
        )
        return oauth.google

    def authorize(self, callback_url, next_url=None):
        return self.oauth.authorize(callback=callback_url, next=next_url)

    @property
    def authorized_response(self):
        # TODO: if error
        return self.oauth.authorized_response()

    def fetch_account(self):
        # TODO: check authorized_response
        return GoogleAccount(self.authorized_response)

    def is_error(self):
        return self.errors == []

    def _activate_development_mode(self):
        if not current_app.config['DEVELOPMENT']:
            return False
        import os
        # only use local server.
        # allow redirect for http
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


class GoogleAccount:
    def __init__(self, authorized_response):
        self.credential = authorized_response
        self.profile = self._fetch_profile()

    @property
    def access_token(self):
        return self.credential['access_token']

    @property
    def email(self):
        return self.profile['email']

    def verify_organization(self):
        if ('hd' in self.profile and
                self.profile['hd'] == current_app.config['GOOGLE_APPS_DOMAIN']):
            return True
        return False

    def _fetch_profile(self):
        # TODO: if error
        end_point = 'https://www.googleapis.com/oauth2/v1/userinfo'
        headers = {'Authorization': 'OAuth {}'.format(self.access_token)}
        response = requests.get(end_point, headers=headers)
        return response.json()
