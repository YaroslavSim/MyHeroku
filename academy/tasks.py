"""Tasks."""
import os

from celery import shared_task

from sendgrid import SendGridAPIClient

from sendgrid.helpers.mail import Mail

from hillel_lesson.settings import EMAIL_SENDER, SENDGRID_API_KEY


@shared_task
def send_email(data):
    """Send email function."""
    message = Mail(
        from_email='{}'.format(data['email']),
        to_emails=EMAIL_SENDER,
        subject='New message from {}'.format(data['name']),
        html_content='<strong>Name: {}<br>Message: {}</strong>'.format(data['name'], data['message'])
        )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
