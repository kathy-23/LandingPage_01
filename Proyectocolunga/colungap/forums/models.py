from django.db import models
from django.conf import settings


class Coment(models.Model):
    id = models.IntegerField(primary_key=True)#id del comentario
    content = models.TextField(max_length=3000)#contenido del comentario
    created_at = models.DateTimeField(auto_now_add=True)#esto guarda una unica vez la fecha en la que se hace el registro
    updated_at = models.DateTimeField(auto_now=True)#esto modifica el registro cada vez que hace una edicion
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#en caso de borrarse 


class Forums(models.Model):
    id = models.IntegerField(primary_key=True)#id del foro
    title = models.CharField(max_length=200)#titulo del foro
    descripcion = models.CharField(max_length=2000)#descripcion del foro
    created_at = models.DateTimeField(auto_now_add=True)#esto guarda una unica vez la fecha en la que se hace el registro
    updated_at = models.DateTimeField(auto_now=True)#esto modifica el registro cada vez que hace una edicion
    id_coment = models.ForeignKey(Coment, on_delete=models.CASCADE)#id del comentario
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#id del usuario


class Topics(models.Model):
    id = models.IntegerField(primary_key=True)#id del topico
    title = models.CharField(max_length=600)#titulo del topíco
    created_at = models.DateTimeField(auto_now_add=True)#esto guarda una unica vez la fecha en la que se hace el registro
    updated_at = models.DateTimeField(auto_now=True)#esto modifica el registro cada vez que hace una edicion
    id_forum=models.ForeignKey(Forums, on_delete=models.CASCADE)#id de los foros que pertenecen el topico






