from django import forms
from .models import WorkSchedule


class WorkScheduleForm(forms.ModelForm):

    class Meta:
        model = WorkSchedule
        fields = ['dateFrom','timeFrom','timeTo','user']
