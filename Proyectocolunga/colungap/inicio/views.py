from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User, AbstractUser 
from anuncios.models import Anuncio
from editadmin.models import Miembro


def inicio(request,redir=""):
    if request.method == 'POST':
        if request.POST.get("btn_logout")=="logout":
            logout(request)
            return redirect('main')
    usuario =User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    anuncios = Anuncio.objects.all().order_by('-fecha')
    #return HttpResponse('<h1>'+str(request.user.id)+'</h1>')
    #return HttpResponse('<h1>'+str(usuario.is_staff)+'</h1>')
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
    elif redir=='inicio-hub.html':
        return redirect('hub')
    return render(request, 'inicio.html',{
        'Is_super':usuario,
        'Anuncios':anuncios,
        'username':username,
        'userid': request.user.id,
        'is_staff':usuario.is_staff
    })
def hub(request,redir=""):
    '''
    if request.method == 'POST':
        if request.POST.get("btn_logout")=="logout":
            logout(request)
            return redirect('main')
    usuarioslist = []
    usuarioslistaux = []
    usuarios = Miembro.objects.filter(cargo='Representante')
    usuarios=list(usuarios)
    ant=""
    for usuario in usuarios:
        orgusu=usuario
        if orgusu == ant:
            pass
        else:
            for usuario in usuarios:
                if usuario.organizacion==orgusu.organizacion:
                    usuarioslistaux.append(usuario)
                    usuarios.pop(usuario)
                else:
                    pass
            usuarioslist.append(usuarioslistaux)
            ant=orgusu
        usuarioslistaux.clear()
    print(usuarioslist)
    '''
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
    return render(request, 'inicio-hub.html',{
    })