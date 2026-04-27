from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Ім'я користувача",
        error_messages={'required': "Це поле обов'язкове."},
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Введіть логін'
        })
    )
    password = forms.CharField(
        label="Пароль",
        error_messages={'required': "Це поле обов'язкове."},
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Пароль'
        })
    )