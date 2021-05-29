from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Anuncio(models.Model):
    id_anuncio= models.IntegerField(primary_key=True)
    id_autor= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200, unique=True)
    comentario = models.CharField(max_length=2000)
