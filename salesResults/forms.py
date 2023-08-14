from django import forms
from .models import SalesResults


class SalesResultsForm(forms.ModelForm):

    class Meta:
        model = SalesResults
        fields = ['date','price','info','user']
