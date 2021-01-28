from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from time import sleep
from django.contrib.auth.models import User

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(10)
    superusers_emails = User.objects.filter(is_superuser=True).values_list('email')
    print(superusers_emails)
    for email in superusers_emails:
        send_mail('Celery Task Worked!', 'This is proof', 
        'gorgias780@gmail.com',
        email )
    return None
