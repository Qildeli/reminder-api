from django.db import models
from django.utils import timezone

from core import settings


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Task(models.Model):
    title = models.CharField(max_length=245, blank=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title
