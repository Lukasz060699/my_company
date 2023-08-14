# Generated by Django 3.2.9 on 2021-12-07 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='accepted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data wakacji'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
        migrations.DeleteModel(
            name='WorkSchedule',
        ),
    ]
