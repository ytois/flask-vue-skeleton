from flask_classy import FlaskView, route
from root_app.tasks import run_task


class TaskView(FlaskView):
    @route('/task_01', methods=['POST'])
    def task_01(self):
        res = run_task.delay()
        res.wait()
        return res.get()
