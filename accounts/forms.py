from django.contrib.auth import forms
from .models import User


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = '__all__'


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User