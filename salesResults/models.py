from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Wyniki sprzedażowe
class SalesResults(models.Model):
    class Meta:
        db_table = 'sales_results'

    id = models.AutoField(primary_key=True)
    date = models.DateField("Data sprzedaży", default=timezone.now)
    price = models.IntegerField("Cena",default=1)
    info = models.TextField("Szczegółowy opis")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
