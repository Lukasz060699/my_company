from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Dni wolne od pracy
class Vacation(models.Model):
    class Meta:
        db_table = 'vacation'

    id = models.AutoField(primary_key=True)
    dateFrom = models.DateField("Data wakacji od", default=timezone.now)
    dateTo = models.DateField("Data wakacji do", default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Użytkownik",  null=True)
    accepted = models.BooleanField("Zakceptowany", default=False, blank=True)
    message = models.TextField("Wiadomość dla moderatora",null=True, blank=True)
