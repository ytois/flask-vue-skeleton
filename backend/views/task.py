from flask import Blueprint
from tasks import run_task


Task = Blueprint('task', __name__)


@Task.route('/some_task')
def index():
    res = run_task.delay()
    res.wait()
    return res.get()
