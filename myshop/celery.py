import os
from celery import Celery
from django.conf import settings
#Основные настройки джанго для сендерея
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myshop.settings')
app=Celery('myshop')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

@app.task
def func(x,y):
    return x+y
