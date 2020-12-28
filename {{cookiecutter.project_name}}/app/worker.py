import os
from celery import Celery


app = Celery(include=('tasks',))
app.conf.beat_schedule = {
    'refresh': {
        'task': 'print_some_stuff',
        'schedule': 10.0,
    },
}