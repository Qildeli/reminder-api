from django.db import models
from django.utils import timezone

from core import settings


class ToDo(models.Model):
    title = models.CharField(max_length=245, blank=False, db_index=True)
    todo = models.CharField(max_length=2000, null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    due_date = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todos", null=False)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title
