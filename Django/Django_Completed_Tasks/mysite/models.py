from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} {self.description}"
