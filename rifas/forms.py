from django import forms
from .models import Rifa


class RifaForm(forms.ModelForm):
    class Meta:
        model = Rifa
        fields = '__all__'