from django.db import models
from django.contrib.auth.models import User
class Miembro(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    cargo=models.CharField(max_length=20)
    organizacion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=12)
# Create your models here.
