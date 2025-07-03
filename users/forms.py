from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'endereco', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',
            'email': 'E-mail',
            'endereco': 'Endereço',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }