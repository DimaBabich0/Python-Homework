from django.db import models

# Create your models here.
class Client(models.Model):
  first_name = models.CharField(max_length=64)            # Идентификатор можно не создавать,
  last_name = models.CharField(max_length=64)             # Django автоматически создаст поле id
  register_at = models.DateTimeField()                    # 
  