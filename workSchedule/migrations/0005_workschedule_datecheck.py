# Generated by Django 3.2 on 2021-12-19 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workSchedule', '0004_auto_20211219_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='workschedule',
            name='dateCheck',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
