from django.db import models
from rest_framework import serializers


class Job(models.Model):
    STATUSES = (
        ('pending', 'pending'),
        ('started', 'started'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    id = serializers.IntegerField(read_only=True)
    status = models.CharField(choices=STATUSES, max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    argument = models.PositiveIntegerField()
    result = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import runSimulation
            runSimulation.delay(job_id=self.id, n=self.argument)