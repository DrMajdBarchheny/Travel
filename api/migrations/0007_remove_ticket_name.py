# Generated by Django 4.2.6 on 2023-10-23 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_ticket_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='name',
        ),
    ]
