from tickets.models import Ticket
from tickets.qr import generate_ticket_qr
from tickets.pdf_generator import generate_ticket_pdf
from tickets.utils import generate_numeric_code
from notifications.services.sms_service import send_and_log_sms
from notifications.utils import build_ticket_sms

def create_ticket(event, attendee):
    ticket = Ticket.objects.create(
        numeric_code = generate_numeric_code(),
        event=event,
        attendee=attendee
    )

    # Generate QR first
    generate_ticket_qr(ticket)
    ticket.save()

    # Generate PDF after QR exists
    ticket.pdf_ticket = generate_ticket_pdf(ticket)
    ticket.save()

    # send SMS
    message = build_ticket_sms(ticket.event, ticket.attendee, ticket)
    send_and_log_sms(ticket.attendee.phone_number, message)
    
    return ticket

