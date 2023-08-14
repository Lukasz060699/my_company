from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=('User'))
    balance = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    info = models.TextField("Historia punktów dodanych przez moderatorów/adminów", blank=True, null =True)
    def __str__(self):
        return self.user.username



# Program lojalnościowy
class LoylalityProgram(models.Model):
    class Meta:
        db_table = 'loylality_program'

    id = models.AutoField(primary_key=True)
    title = models.CharField("Tytuł", max_length=50)
    date = models.DateField("Data zakupu", null=True, blank=True)
    price = models.IntegerField("Cena punktowa",default=1)
    info = models.TextField("Szczegółowy opis nagrody")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



