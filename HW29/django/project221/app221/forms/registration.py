from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone

class RegistrationForm(forms.Form):
    username = forms.CharField(
        label="Ім'я користувача",
        max_length=150,
        error_messages={
            'required': "Це поле обов'язкове.",
            'max_length': "Ім'я користувача не може бути довшим за 150 символів."
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Введіть логін'
        })
    )
    email = forms.EmailField(
        label="Email",
        error_messages={
            'required': "Це поле обов'язкове.",
            'invalid': "Введіть коректну email адресу."
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'name@example.com'
        })
    )
    password = forms.CharField(
        label="Пароль",
        error_messages={
            'required': "Це поле обов'язкове."
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Пароль'
        })
    )
    confirm_password = forms.CharField(
        label="Підтвердження пароля",
        error_messages={
            'required': "Це поле обов'язкове."
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Повторіть пароль'
        })
    )
    birth_date = forms.DateField(
        label="Дата народження",
        error_messages={
            'required': "Це поле обов'язкове.",
            'invalid': "Введіть коректну дату."
        },
        widget=forms.DateInput(attrs={
            'class': 'form-control', 'type': 'date'
        })
    )

    GENDER_CHOICES = [
        ('M', 'Чоловік'),
        ('F', 'Жінка')
    ]
    gender = forms.ChoiceField(
        label="Стать",
        choices=GENDER_CHOICES,
        error_messages={
            'required': "Це поле обов'язкове.",
            'invalid_choice': "Оберіть коректну опцію."
        },
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    interests = forms.MultipleChoiceField(
        label="Інтереси",
        required=False,
        choices=[
            ('python', 'Python'),
            ('django', 'Django'),
            ('data', 'Data Science'),
            ('web', 'Web'),
        ],
        widget=forms.CheckboxSelectMultiple()
    )

    agree_terms = forms.BooleanField(
        label="Погоджуюсь з умовами",
        required=True,
        error_messages={
            'required': "Ви повинні погодитися з умовами."
        },
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    bio = forms.CharField(
        label="Про себе",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'rows': 3, 'placeholder': 'Коротко про себе'
        })
    )

    def clean_username(self):
        u = self.cleaned_data['username']
        if User.objects.filter(username=u).exists():
            raise ValidationError("Користувач із таким іменем вже існує.")
        return u

    def clean(self):
        cleaned = super().clean()
        p = cleaned.get('password')
        cp = cleaned.get('confirm_password')
        if p and cp and p != cp:
            self.add_error('confirm_password', "Паролі не співпадають.")
        birth = cleaned.get('birth_date')
        if birth and birth > timezone.now().date():
            self.add_error('birth_date', "Дата народження не може бути в майбутньому.")
        return cleaned
