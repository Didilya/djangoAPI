from celery import shared_task
from django.core.mail import send_mail
from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!', 'This is proof', 
    'gorgias780@gmail.com',
     ['diniwag728@aiclbd.com'] )
    return None
