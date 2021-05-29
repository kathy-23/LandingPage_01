from django.db import models
from django.conf import settings


class Topics(models.Model):
    id = models.IntegerField(primary_key=True)#id del topico
    title = models.CharField(max_length=600)#titulo del topíco
    created_at = models.DateTimeField(auto_now_add=True)#esto guarda una unica vez la fecha en la que se hace el registro
    updated_at = models.DateTimeField(auto_now=True)#esto modifica el registro cada vez que hace una edicion
    
class Forums(models.Model):
    id = models.IntegerField(primary_key=True)#id del foro
    title = models.CharField(max_length=200,unique=True)#titulo del foro
    descripcion = models.CharField(max_length=2000)#descripcion del foro
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#id del usuario que creo el foro
    id_topic=models.ForeignKey(Topics, on_delete=models.CASCADE)#id del topico al que pertenecen el foro
    cant_coment = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)#esto guarda una unica vez la fecha en la que se hace el registro
    updated_at = models.DateTimeField(auto_now=True)#esto modifica el registro cada vez que hace una edicion
    

class Coment(models.Model):
    id = models.IntegerField(primary_key=True)#id del comentario
    content = models.TextField(max_length=3000,blank=True,null=True)#contenido del comentario
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#en caso de borrarse 
    id_forum= models.ForeignKey(Forums, on_delete=models.CASCADE)
    padre = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)#esto guarda una unica vez la fecha en la que se hace el registro
    

