from flask.views import MethodView
from root_app.tasks import run_task


class TaskView(MethodView):
    def post(self):
        res = run_task.delay()
        res.wait()
        return res.get()
