from apps.models import User
from apps.tasks import task_send_email


def sms_to_users():
    emails: list = User.objects.values_list('email', flat=True)
    text = 'Add new products'
    task_send_email.delay('Testing Users', text, list(emails))
