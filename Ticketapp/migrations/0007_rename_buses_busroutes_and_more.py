# Generated by Django 4.0.2 on 2022-05-18 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketapp', '0006_buses_active_car_active_ticket_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buses',
            new_name='Busroutes',
        ),
        migrations.RenameField(
            model_name='ticket_details',
            old_name='Buses',
            new_name='Busroutes',
        ),
    ]
