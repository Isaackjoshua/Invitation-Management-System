from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_checked_in_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='checked_in_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
