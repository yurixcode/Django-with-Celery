from __future__ import absolute_import
import time
from .celery import app
from .models import Job

@app.task
def hello(name):
    print('Hello!') 
    time.sleep(10)
    print('Hello ', name )