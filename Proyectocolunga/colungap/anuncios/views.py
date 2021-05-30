from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect, render, HttpResponse
from .models import Anuncio
from .forms import addanuncio
# Create your views here.

def addAnuncio(request, redir=''):
    usuario =User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    anuncios = Anuncio.objects.all().order_by('-fecha')
    formulario=addanuncio(request.POST)
    if request.method == 'POST':
        if request.POST.get("showAgregar") == "True":
            return render(request, 'inicio-anuncios.html', {
                'formulario': formulario,
                'showAgregar': 'True',
                'showAnuncio': 'False',
                'userid' : request.user.id,
                'username':username,
            })
        if request.POST.get("boton_agregar") == "True":
            if formulario.is_valid():
                Anuncio.objects.create(
                    id_autor_id= request.user.id,
                    titulo = request.POST.get("titulo"),
                    comentario = request.POST.get("comentario")
                )
                return render(request, 'inicio-anuncios.html', {
                'Anuncios':anuncios,
                'showAgregar': 'False',
                'showAnuncio': 'True',
                'userid' : request.user.id,
                'username':username,
            })
        if request.POST.get("del_anuncio")=='True':
            anuncio = Anuncio.objects.get(id_anuncio=request.POST.get("id_anuncio"))
            anuncio.delete()
            return render(request, 'inicio-anuncios.html', {
                'Anuncios':anuncios,
                'showAgregar': 'False',
                'showAnuncio': 'True',
                'del_anuncio': 'False',
                'userid' : request.user.id,
                'username':username,
            })
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
    return render(request, 'inicio-anuncios.html',{
        'Anuncios': anuncios,
        'showAnuncio':"True",
        'userid' : request.user.id,
        'username':username,
    })