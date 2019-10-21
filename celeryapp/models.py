from django.db import models


class Job(models.Model):
    STATUSES = (
        ('started', 'started'),
        ('pending', 'pending'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    status = models.CharField(choices=STATUSES, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    argument = models.PositiveIntegerField()
    result = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import hello
            hello.delay(n=self.argument)