from django.shortcuts import render, redirect,HttpResponse

from django.contrib.auth.models import User, AbstractUser 
from anuncios.models import Anuncio


def inicio(request,redir=""):
    usuario =User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    anuncios = Anuncio.objects.all().order_by('-fecha')
    #return HttpResponse('<h1>'+str(request.user.id)+'</h1>')
    if redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    elif redir=='inicio-anuncios.html':
        return redirect('inicio_anuncios')
    elif redir=='inicio-topicos.html':
        return redirect('inicio_topicos')
    return render(request, 'inicio.html',{
        'Anuncios':anuncios,
        'username':username,
        'userid': request.user.id,
    })
     