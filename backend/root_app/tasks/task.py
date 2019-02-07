from worker import celery


@celery.task(name='some_task')
def run_task():
    print('run_task')
    return 'done.'
