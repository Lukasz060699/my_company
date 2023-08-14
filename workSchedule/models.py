from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

# Dni pracy
class WorkSchedule(models.Model):
    class Meta:
        db_table = 'work_schedule'

    id = models.AutoField(primary_key=True)
    dateFrom = models.DateField("Pracuje od dnia", default=timezone.now)
    timeFrom = models.TimeField("Pracuje od godziny", default=datetime.now)
    timeTo = models.TimeField("Pracuje do godziny", default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
