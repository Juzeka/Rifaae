from django import forms
from .models import Bilhete


class BilheteForm(forms.ModelForm):
    class Meta:
        model = Bilhete
        fields = '__all__'