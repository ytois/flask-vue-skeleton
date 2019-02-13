from flask import Blueprint
from .views import IndexView, LoginView, TaskView

ROUTE_BASE = '/'

app = Blueprint('root', __name__, template_folder='templates')

IndexView.register(app, route_base=ROUTE_BASE)
TaskView.register(app, route_base=ROUTE_BASE, route_prefix='/tasks')
LoginView.register(app, route_base=ROUTE_BASE)
