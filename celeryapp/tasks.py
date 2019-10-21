from __future__ import absolute_import
from functools import wraps
import time
from .celery import app
from .models import Job

# decorator to avoid code duplication
def update_job(fn):  
    """Decorator that will update Job with result of the function"""

    # wraps will make the name and docstring of fn available for introspection
    @wraps(fn)
    def wrapper(job_id, *args, **kwargs):
        job = Job.objects.get(id=job_id)
        job.status = 'started'
        job.save()
        try:
            # execute the function fn
            result = fn(*args, **kwargs)
            job.result = result
            job.status = 'finished'
            job.save()
        except:
            job.result = None
            job.status = 'failed'
            job.save()
    return wrapper

@app.task
@update_job
def runSimulation(n):
    print('Starting simulation') 
    time.sleep(20)
    print('Simulation finished')
    return n + 10