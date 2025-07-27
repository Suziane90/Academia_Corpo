from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        filds = ('username', 'email', 'telefone', 'foto')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        filds = ('username', 'email', 'telefone', 'foto')