from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from django.conf import settings
import os

PRIMARY_COLOR = HexColor("#0A2540")   # dark blue
ACCENT_COLOR = HexColor("#F2F4F7")    # light gray


def generate_ticket_pdf(ticket):
    file_name = f"{ticket.numeric_code}.pdf"
    file_path = os.path.join(settings.MEDIA_ROOT, "pdf_tickets", file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # ---------------- HEADER ----------------
    c.setFillColor(PRIMARY_COLOR)
    c.rect(0, height - 120, width, 120, stroke=0, fill=1)

    # Logo
    logo_path = os.path.join(settings.MEDIA_ROOT, "branding/logo.png")
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 60, height - 95, width=120, height=60, mask="auto")

    # Event name
    c.setFillColor("white")
    c.setFont("Helvetica-Bold", 22)
    c.drawRightString(width - 60, height - 70, ticket.event.name)

    # ---------------- BODY ----------------
    c.setFillColor("black")
    c.setFont("Helvetica", 12)

    start_y = height - 180
    line_gap = 28

    c.drawString(80, start_y, "Attendee Name")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(80, start_y - 20, ticket.attendee.full_name)

    c.setFont("Helvetica", 12)
    c.drawString(80, start_y - line_gap * 2, "Event Location")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(80, start_y - line_gap * 2 - 20, ticket.event.location)

    c.setFont("Helvetica", 12)
    c.drawString(80, start_y - line_gap * 4, "Ticket Code")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(80, start_y - line_gap * 4 - 22, ticket.numeric_code)

    # ---------------- QR SECTION ----------------
    c.setFillColor(ACCENT_COLOR)
    c.roundRect(width - 300, start_y - 180, 200, 240, 12, stroke=0, fill=1)

    if ticket.qr_code_image:
        c.drawImage(
            ticket.qr_code_image.path,
            width - 270,
            start_y - 150,
            width=140,
            height=140
        )

    c.setFillColor("black")
    c.setFont("Helvetica", 10)
    c.drawCentredString(width - 200, start_y - 170, "Scan at entry")

    # ---------------- FOOTER ----------------
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor("#555555")
    c.drawCentredString(
        width / 2,
        40,
        "This ticket is valid for one entry only. Duplicate scans will be rejected."
    )

    c.showPage()
    c.save()

    return f"pdf_tickets/{file_name}"
