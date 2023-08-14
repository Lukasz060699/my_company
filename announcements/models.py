from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Ogłoszenia
class Announcements(models.Model):
    class Meta:
        db_table = 'announcements'

    id = models.AutoField(primary_key=True)
    title = models.CharField("Tytuł ogłoszenia", max_length=50)
    text = models.TextField("Treść ogłoszenia")
    date = models.DateTimeField(default=timezone.now, editable=False)

