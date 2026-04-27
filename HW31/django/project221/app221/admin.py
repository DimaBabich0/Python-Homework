from django.contrib import admin
from .models import *
  
# Register your models here.

# admin.site.register(Client) # Модель работает, но только по умолчанию

class ClientAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'register_at') # отображаемые поля в админке

admin.site.register(Client, ClientAdmin) # Регистрируем модель с кастомным отображением в админке