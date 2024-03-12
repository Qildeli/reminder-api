from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from .models import ToDo
from django.conf import settings


@shared_task(name='send_email')
def send_remainder_email():
    """
    Check if one hour remains until the task deadline and send an email notification if true.
    """

    one_hour_from_now = timezone.now() + timedelta(hours=1)

    todos_to_notify = ToDo.objects.filter(deadline__lte=one_hour_from_now, notified=False)

    for todo in todos_to_notify:

        send_mail(
            subject=f"Reminder for {todo.title}",
            message="This is a reminder for your pending task.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[todo.owner.email],
            fail_silently=False
        )
        todo.notified()
        todo.save()
