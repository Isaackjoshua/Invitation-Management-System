from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.conf import settings
import os

def generate_ticket_pdf(ticket):
    file_name = f"{ticket.numeric_code}.pdf"
    file_path = os.path.join(settings.MEDIA_ROOT, "pdf_tickets", file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 80, "EVENT TICKET")

    # Event Info
    c.setFont("Helvetica", 12)
    c.drawString(80, height - 140, f"Event: {ticket.event.name}")
    c.drawString(80, height - 170, f"Location: {ticket.event.location}")
    c.drawString(80, height - 200, f"Attendee: {ticket.attendee.full_name}")
    c.drawString(80, height - 230, f"Ticket Code: {ticket.numeric_code}")

    # QR Image
    if ticket.qr_code_image:
        qr_path = ticket.qr_code_image.path
        c.drawImage(qr_path, width - 240, height - 320, width=160, height=160)

    c.showPage()
    c.save()

    return f"pdf_tickets/{file_name}"
