import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sib_cafee.settings.dev')

celery = Celery('sib_cafee')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()