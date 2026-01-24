from django.db import models

class CheckIn(models.Model):
    ticket = models.ForeignKey('tickets.Ticket', on_delete=models.CASCADE)
    staff = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    
# Create your models here.
