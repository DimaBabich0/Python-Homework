from . import views
from django.urls import path

urlpatterns = [
  path('hello/', views.hello, name='hello'),
  path('', views.index, name='index'),
  path('intro/', views.intro, name='intro'),
  path('privacy/', views.privacy, name='privacy'),
]
