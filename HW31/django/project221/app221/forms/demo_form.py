from django import forms
from django.core.exceptions import ValidationError

class DemoForm(forms.Form):
  first_name = forms.CharField(
    min_length=2,
    max_length=30,
    label='First name',
    error_messages={
      'required': "Это поле обязательно для заполнения",
      'min_length': "Имя должно быть не менее 2 символов",
      'max_length': "Имя должно быть не более 30 символов",
    }
  )
  last_name = forms.CharField(
    min_length=2,
    max_length=30,
    label='Last name',
    error_messages={
      'required': "Это поле обязательно для заполнения",
      'min_length': "Фамилия должна быть не менее 2 символов",
      'max_length': "Фамилия должна быть не более 30 символов",
    }
  )

  def clean(self):                     # метод, который отвечает за валидацию формы
    cleaned_data = super().clean()     # запуск обработки по умолчанию
    # если поле проходит валидацию, то оно добавляется в cleaned_data
    if 'first_name' in cleaned_data:   # если проходит базовую валидацию, то добавляем
      # свою проверку, например, что имя должно начинаться с заглавной буквы
      first_name = cleaned_data['first_name'] # берем за основу значеение, что прошло проверку
      # проверяем, что первая буква - заглавная
      if not first_name[0].isupper():
        self.add_error('first_name', ValidationError("Имя должно начинаться с заглавной буквы"))

      last_name = cleaned_data['last_name']
      if not last_name[0].isupper():
        self.add_error('last_name', ValidationError("Фамилия должна начинаться с заглавной буквы"))