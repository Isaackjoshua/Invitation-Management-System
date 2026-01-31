import africastalking
from django.conf import settings

africastalking.initialize(
    settings.AT_USERNAME,
    settings.AT_API_KEY
)

sms = africastalking.SMS


def send_ticket_sms(phone_number: str, message: str):
    """
    Low-level SMS sender.
    Raises exception if provider fails.
    """
    return sms.send(
        message=message,
        recipients=[phone_number]
    )
