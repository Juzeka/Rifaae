from django import forms
from .models import Logradouro


class LogradouroForm(forms.ModelForm):
    class Meta:
        model = Logradouro
        fields = '__all__'