from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=245, blank=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
