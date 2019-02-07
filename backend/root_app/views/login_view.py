from flask import redirect
from flask.views import MethodView


class LoginView(MethodView):
    def get(self):
        return 'login'

    def post(self):
        return redirect('/')

    def delete(self):
        return redirect('/')
