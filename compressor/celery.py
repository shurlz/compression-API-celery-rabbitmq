from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'compressor.settings')

# app = Celery('tasks', broker='pyamqp://guest@localhost//')

app = Celery('compressor')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send_email_confirmations':{
        'task':'base.tasks.send_confirmations',
        'schedule': 60 * 4,
    },
}

app.autodiscover_tasks()
