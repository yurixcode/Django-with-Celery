from __future__ import absolute_import

from celeryapp.tasks import update_job

import time
import random

from celeryapp.celery import app
from celeryapp.models import Job


@app.task
def generateExcel():
    print('Generating file') 
    time.sleep(random.randint(1, 60))
    print('End')
    return random.randint(1, 100)