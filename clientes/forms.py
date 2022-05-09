from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        # widgets = {
        #     'nome': forms.TextInput(attrs={'class': 'form-control'}),
        #     'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
        #     'cpf': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'celular': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'logradouro': forms.Select(attrs={'class': 'form-select'}),
        #     'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        # }