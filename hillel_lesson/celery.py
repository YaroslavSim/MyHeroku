"""Celery."""
import os

from celery import Celery

from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hillel_lesson.settings')

app = Celery('hillel_lesson')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.conf.beat_schedule = {
    'run_every_day': {
        'task': 'logger.tasks.delete_logs',
        'schedule': crontab(minute=0, hour=0),
        'args': (),
    }
}

app.conf.beat_schedule = {
    'get_exchange_rates': {
        'task': 'exchanger.tasks.get_exchange_rates',
        'schedule': 1800.0
    }
}

app.autodiscover_tasks()
