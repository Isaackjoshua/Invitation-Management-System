from tickets.models import Ticket
from tickets.qr import generate_ticket_qr
from tickets.pdf_generator import generate_ticket_pdf
from tickets.utils import generate_numeric_code

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

    return ticket
