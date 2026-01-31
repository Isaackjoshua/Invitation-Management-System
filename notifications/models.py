from django.db import models

class SMSLog(models.Model):
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.status}"
