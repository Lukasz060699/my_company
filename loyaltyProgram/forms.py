from django import forms
from .models import LoylalityProgram


class LoylalityProgramForms(forms.ModelForm):

    class Meta:
        model = LoylalityProgram
        fields = ['price','title','info']
