from notifications.models import SMSLog
from notifications.services.sms_provider import send_ticket_sms


def send_ticket_sms(phone_number, message):
    print("SMS TO:", phone_number)
    print("MESSAGE:", message)
    return {"status": "MOCK_SENT"}

# def send_and_log_sms(phone_number: str, message: str):
#    try:
#       response = send_ticket_sms(phone_number, message)
#        status = "SENT"
#    except Exception as e:
#        response = str(e)
#        status = "FAILED"
#
#    SMSLog.objects.create(
#        phone_number=phone_number,
#        message=message,
#        status=status
#    )

#    return {
#        "status": status,
#        "response": response
#    }
