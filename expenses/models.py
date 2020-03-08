# Django
from django.conf import settings
from django.db import models


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=25, decimal_places=3)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.cost}'