# Generated by Django 3.2.9 on 2021-12-07 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='text',
            field=models.TextField(verbose_name='Treść ogłoszenia'),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Tytuł ogłoszenia'),
        ),
    ]
