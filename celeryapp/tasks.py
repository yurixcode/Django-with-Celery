from __future__ import absolute_import
import time
from celery import shared_task

@shared_task
def hello(name):
    print('Hello!') 
    time.sleep(10)
    print('Hello ', name ) 