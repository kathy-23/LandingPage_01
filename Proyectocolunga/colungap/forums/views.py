from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login ,logout 
from .models import Coment, Forums, Topics
from .forms import addForum

def inicio_topicos(request,redir=""):
    '''acciones al cargar la pagina'''
    navtopicos=Topics.objects.all()
    #formulario de añadir foro
    formaddForum=addForum(request.POST)
    #condiciones para un post
    if request.method == 'POST':
    #accion si se apreta crear nuevo foro
        if request.POST.get('showaddforum')=='True':
            #tamaño de la lista de topicos
            cant_topicos="size="+str(len(Topics.objects.all()))
            return render(request,'inicio-topicos.html',{
                'navtopicos':navtopicos,
                'foros':"False",
                'showaddforum':"True",
                'cant_topicos':cant_topicos,
                'formaddForum':formaddForum
            })
        
        #accion si se apreta el agregar foro
        if request.POST.get('addforum')=='True':
            #obtengo el topico seleccionado
            topico=Topics.objects.get(title=request.POST.get('topico_seleccionado'))
            #verifico si el llenado de formulario es valido
            if formaddForum.is_valid():
                #return HttpResponse('<h1>'+str(topico.id)+'</h1>')
                #creo y agrego a la bdd usando el modelo de Forums
                Forums.objects.create(
                    title=request.POST.get('titulo'),
                    descripcion=request.POST.get('descripcion'),
                    #los identificadores de las claves foraneas se ponen como estan en la bdd
                    id_user_id=request.user.id,
                    #los identificadores de las claves foraneas se ponen como estan en la bdd
                    id_topic_id=topico.id,
                    cant_coment=0
                )
                #return HttpResponse('<h1>'+str(obj.id_topic_id)+'</h1>')
                return render(request,'inicio-topicos.html',{
                    'navtopicos':navtopicos,
                    'foros':'False',
                    'showaddforum':"False",
                    'addUser':'False',
                    'formaddForum':formaddForum
                })
            else:
                HttpResponse('<h1>no se pudo agregar</h1>')
        #accion si se selecciona un topico
        if request.POST.get('nav_topico'):
            title=request.POST.get('nav_topico')
            topico_seleccionado=Topics.objects.get(title=title)
            #mis foros en ese topico
            misforos=Forums.objects.filter(id_user_id=request.user.id)
            #todos los foros del topico seleccionado
            otrosforos=Forums.objects.filter(id_topic_id=topico_seleccionado.id).exclude(id_user_id=request.user.id)
            #allforos=Forums.objects.all()
            #return HttpResponse('<h1>'+str(len(allforos))+'</h1>')
            for foro in misforos:
                #cantidad de comentarios de mis foros
                foro.cant_coment=len(Coment.objects.filter(id_forum_id=foro.id))
                #guardo el foro
                foro.save()
            for foro in otrosforos:
                #cantidad de comentarios de los otros foros
                foro.cant_coment=len(Coment.objects.exclude(id_forum_id=foro.id))
                #guardo el foro
                foro.save()
            return render(request,'inicio-topicos.html',{
                'navtopicos':navtopicos,
                'foros':'True',
                'showaddforum':"False",
                'addUser':'False',
                'topico_seleccionado':topico_seleccionado,
                'misforos':misforos,
                'otrosforos':otrosforos,
            })
        if request.POST.get("foro_seleccionado"):
            return comentforo(request)
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
    return render(request,'inicio-topicos.html',{
        'navtopicos':navtopicos,
        'foros':'False',
        'showaddforum':"False",
        'addUser':'False',
    })


def comentforo(request):
    idforo = request.POST.get("foro_seleccionado")
    foro=Forums.objects.get(id=idforo)
    comentarios=Coment.objects.filter(id_forum_id=foro.id)
    userid = request.user.id
    #return HttpResponse('<h1>'+str(foro.title)+'</h1>')
    if request.method == 'POST':
        if request.POST.get("deletecoment"):
            comentario=Coment.objects.get(id=request.POST.get("deletecoment"))
            comentario.delete()
            return render(request,'comentforo.html',{
                'foro':foro,
                'comentarios':comentarios,
                'userid':userid,
    })
            #obtengo todos los comentarios de este foro
    return render(request,'comentforo.html',{
        'foro':foro,
        'comentarios':comentarios,
        'userid':userid,
    })
