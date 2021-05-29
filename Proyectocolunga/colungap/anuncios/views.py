from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect, render, HttpResponse
from .models import Anuncio
from .forms import addanuncio
# Create your views here.

def addAnuncio(request, redir=''):
    usuarios = request.user.id
    anuncios = Anuncio.objects.all()
    formulario=addanuncio(request.POST)
    if request.method == 'POST':
        if request.POST.get("showAgregar") == "True":
            return render(request, 'inicio-anuncios.html', {
                'formulario': formulario,
                'showAgregar': 'True',
                'showAnuncio': 'False'
            })
        if request.POST.get("boton_agregar") == "True":
            if formulario.is_valid():
                Anuncio.objects.create(
                    id_autor_id= usuarios,
                    titulo = request.POST.get("titulo"),
                    comentario = request.POST.get("comentario")
                )
                return render(request, 'inicio-anuncios.html', {
                'Anuncios':anuncios,
                'showAgregar': 'False',
                'showAnuncio': 'True'
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
        'showAnuncio':"True"
    })