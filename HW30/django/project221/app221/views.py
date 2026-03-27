from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import django
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .forms.demo_form import DemoForm
from .forms.registration import RegistrationForm
from .forms.login import LoginForm

def hello(request):
  return HttpResponse('Hello, world!')


def index(request):
  template = loader.get_template('index.html') # директория - автоматически подставляется
  context = {                           # Переденный до шаблона словарь с данными
    'x': 42,                            # автоматически превращаются в переменные шаблона,
    'str': 'Hello world!',              # которые можно использовать в шаблоне
    'list': [1, 2, 3],                  # путем указания имени переменной
    'dict': {'a': 1, 'b': 2, 'c': 3},   # в двойных фигурных скобках {{ имя_переменной }}
    'bool': True,                       # 
    'none': None,                       #
  }
  print(request)
  return HttpResponse(template.render(context=context, request=request))


def intro(request):
  template = loader.get_template('intro.html')
  now = datetime.now()
  load_time = now.strftime("%H:%M %d.%m.%Y")
  context = {
    'django_version': django.get_version(),
    'load_time': load_time,
  }
  return HttpResponse(template.render(context=context, request=request))


def privacy(request):
  template = loader.get_template('privacy.html')
  now = datetime.now()
  update_date = now.strftime("%d.%m.%Y")
  context = {
    'update_date': update_date,
  }
  return HttpResponse(template.render(context=context, request=request))


def forms(request):
  template = loader.get_template('forms.html')
  context = {
    'get': str(request.GET),                             # словарь с query-параметрами
    'x': request.GET.get('x', None),                     # доступ к X query-параметров
    'demo_form': DemoForm() if request.method == 'GET'   #
      else DemoForm(request.POST),                       # экземпляр формы для рендера в шаблоне
  }
  return HttpResponse(template.render(context=context, request=request))


def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      User.objects.create_user(
        username=form.cleaned_data['username'],
        email=form.cleaned_data['email'],
        password=form.cleaned_data['password']
      )
      messages.success(request, "Реєстрація пройшла успішно! Тепер ви можете увійти.")
      return redirect('login')
    else:
      messages.error(request, "Будь ласка, виправте помилки у формі.")
  else:
    form = RegistrationForm()

  return render(request, 'registration.html', {'form': form})


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      if user is not None:
        auth_login(request, user)
        messages.success(request, "Вхід успішний!")
        return redirect('index')
      else:
        messages.error(request, "Невірне ім'я користувача або пароль.")
  else:
    form = LoginForm()

  return render(request, 'login.html', {'form': form})



