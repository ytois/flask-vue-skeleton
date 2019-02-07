from flask import Blueprint
from .views import IndexView, LoginView, TaskView

app = Blueprint('root', __name__, template_folder='templates')

login_view = LoginView.as_view('login_view')

app.add_url_rule(
    '/', view_func=IndexView.as_view('index_view'), methods=['GET'])
app.add_url_rule('/login', view_func=login_view,
                 methods=['GET', 'POST'])
app.add_url_rule(
    '/logout', view_func=login_view, methods=['DELETE'])
app.add_url_rule(
    '/some_task', view_func=TaskView.as_view('task_view'), methods=['POST'])
