from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail

from .models import Task
from django.conf import settings


@shared_task(name='send_email')
def send_remainder_email():
    """
    Check if one hour remains until the task deadline and send an email notification if true.
    """

    one_hour_date_time = Task.due_date - timedelta(hours=1)

    tasks_to_notify = Task.objects.filter(deadline__lte=one_hour_date_time, notified=False)

    for task in tasks_to_notify:

        send_mail(
            subject=f"Reminder {task.title}",
            message="This is a reminder for your pending task.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[task.owner.email],
            fail_silently=False
        )
        task.notified()
        task.save()
