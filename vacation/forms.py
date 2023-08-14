from django import forms
from .models import Vacation


class VacationForm(forms.ModelForm):

    class Meta:
        model = Vacation
        fields = ['dateFrom','dateTo','message']

class VacationModeratorForm(forms.ModelForm):

    class Meta:
        model = Vacation
        fields = ['dateFrom','dateTo','accepted','message']
