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
        'user':usuario
    })
def hub(request,redir=""):
    usuario =User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    if request.method == 'POST':
        if request.POST.get("btn_logout")=="logout":
            logout(request)
            return redirect('main')
    usuarioslist = []
    listusuaux = []
    usuorg = Miembro.objects.filter(cargo='Representante' or 'representante')
    usuarios=User.objects.exclude(is_active=False).all()
    orglist=[]
    for usuario in usuorg:
        if usuario.organizacion not in orglist:
            orglist.append(usuario.organizacion)
        else:
            pass
    for i in orglist:
        for usuario in usuorg:
            if usuario.organizacion==i:
                listusuaux.append(usuario)
            else:
                pass
        usuarioslist.append(listusuaux)
        listusuaux=[]
    listusuaux=[]
    finallist=[]
    for org in usuarioslist:
        for usu in org:
            for usua in usuarios:
                if usu.user_id==usua.id:
                    listusuaux.append([usua.first_name+" "+usua.last_name,usu.telefono,usua.email,usu.organizacion])
                else:
                    pass
        finallist.append(listusuaux)
        listusuaux=[]
    rangeorglist=[str(i) for i in range(len(orglist))]
    rangeorglist=''.join(rangeorglist)
    #return HttpResponse('<h1>'+str(rangeorglist)+'</h1>')
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
        'datos' : finallist,
        'username': username,
    })