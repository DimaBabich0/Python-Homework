from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import django
from datetime import datetime

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