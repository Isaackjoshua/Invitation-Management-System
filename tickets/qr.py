import qrcode
from django.core.files.base import ContentFile
from io import BytesIO

def generate_ticket_qr(ticket):
    data = f"TICKET:{ticket.numeric_code}"

    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    file_name = f"{ticket.numeric_code}.png"
    ticket.qr_image.save(
        file_name,
        ContentFile(buffer.getvalue()),
        save=False
    )
