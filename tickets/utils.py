from .models import Ticket
import random 
import string

def generate_numeric_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_unique_numeric_code():
    while True:
        code = generate_numeric_code()
        if not Ticket.objects.filter(numeric_code=code).exists():
            return code
