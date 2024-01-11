from django.contrib.auth.forms import UserCreationForm

from django import forms

from .models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'}
        )
    )
    passwor1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    passwor2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')