from django.db import models

class Attendee(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# Create your models here.
