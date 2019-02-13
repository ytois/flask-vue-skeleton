from flask import Blueprint
from .views import IndexView, LoginView, TaskView

app = Blueprint('root', __name__, template_folder='templates')

app.add_url_rule(
    '/', view_func=IndexView.as_view('index_view'), methods=['GET'])
app.add_url_rule(
    '/some_task', view_func=TaskView.as_view('task_view'), methods=['POST'])

LoginView.register(app)
