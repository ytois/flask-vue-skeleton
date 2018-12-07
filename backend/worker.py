from celery import Celery


celery = Celery(
    'worker',
    include='tasks'
)
celery.config_from_object('config.celeryconfig')
