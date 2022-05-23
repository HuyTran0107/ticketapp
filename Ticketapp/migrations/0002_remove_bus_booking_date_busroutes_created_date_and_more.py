# Generated by Django 4.0.2 on 2022-05-21 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='booking_date',
        ),
        migrations.AddField(
            model_name='busroutes',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='busroutes',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
