import uuid
from django.db import models

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    attendee = models.OneToOneField('attendees.Attendee', on_delete=models.CASCADE)

    numeric_code = models.CharField(max_length=8, unique=True)
    is_checked_in = models.BooleanField(default=False)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    numeric_code = models.CharField(
        max_length=8,
        unique = True,
        db_index=True
    )
    class Meta:
         indexes = [
             models.Index(fields=["numeric_code"]),
             models.Index(fields=["is_checked_in"]),
         ]
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["event", "attendee"],
                name="unique_ticket_per_event_attendee"
        )
    ]

    
# Create your models here.
