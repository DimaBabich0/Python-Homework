from . import views
from django.urls import path

urlpatterns = [
  path('hello/', views.hello, name='hello'),
  path('', views.index, name='index'),
  path('intro/', views.intro, name='intro'),
  path('privacy/', views.privacy, name='privacy'),
  path('forms/', views.forms, name='forms'),
  path('registration/', views.registration, name='registration'),
  path('login/', views.login_view, name='login'),
  path('models/', views.models, name='models'),
]
