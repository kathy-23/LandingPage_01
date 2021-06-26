from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import logout 
from .models import Coment, Forums, Topics
from .forms import addForum
from django.contrib.auth.models import User
import time
from django.contrib import messages

def inicio_topicos(request,redir=""):
    usuario =User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    '''acciones al cargar la pagina'''
    navtopicos=Topics.objects.all()
    #formulario de añadir foro
    formaddForum=addForum(request.POST)
    #condiciones para un post
    if request.method == 'POST':
        if request.POST.get("btn_logout")=="logout":
            logout(request)
            return redirect('main')
        #accion si se apreta crear nuevo foro
        if request.POST.get('showaddforum')=='True':
            #tamaño de la lista de topicos
            cant_topicos="size="+str(len(Topics.objects.all()))
            return render(request,'inicio-topicos.html',{
                'navtopicos':navtopicos,
                'foros':"False",
                'showaddforum':"True",
                'cant_topicos':cant_topicos,
                'formaddForum':formaddForum,
                'userid': request.user.id,
                'username':username,
                'is_staff':usuario.is_staff,
            })
        
        #accion si se apreta el acrear foro
        if request.POST.get('addforum')=='True':
            try:
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
                        'formaddForum':formaddForum,
                        'userid': request.user.id,
                        'username':username,
                        'is_staff':usuario.is_staff,
                    })
                else:
                    messages.info(request,'Error al guardar el foro.')
            except:
                messages.info(request,'Error al guardar el foro.')
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
                'userid': request.user.id,
                'username':username,
                'is_staff':usuario.is_staff,
            })
        if request.POST.get("del_foro")=="True":
            forod=Forums.objects.get(id=int(request.POST.get("id_foro")))
            forod.delete()
            topico_seleccionado=Topics.objects.get(id=int(request.POST.get('topico_seleccionado')))
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
                'userid': request.user.id,
                'username':username,
            })
        if request.POST.get("foro_seleccionado"):
            idforo = request.POST.get("foro_seleccionado")
            return redirect('comentforo',idforo)


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
        'userid': request.user.id,
        'username':username,
        'is_staff':usuario.is_staff,
    })


def comentforo(request,**kwargs):
    userid = request.user.id
    user_name=User.objects.get(id=userid)
    username=user_name.first_name+" "+user_name.last_name
    listacomentarios=list()
    idforo=kwargs.get('idforo')
    if kwargs.get('idforo')=='inicio-topicos.html':
        return redirect('inicio_topicos')
    foro=Forums.objects.get(id=idforo)
    comentarios=Coment.objects.filter(id_forum_id=foro.id)

    #codigo para ordenar comentarios poniendo las respuestas debajo del comentario
    for comentario in comentarios:
        if comentario.padre_id==None:
            comentario.padre_id='None'
            listacomentarios.append(comentario)
            for coment in comentarios:
                if coment.padre_id==comentario.id:
                    listacomentarios.append(coment)
                else:
                    pass
        else:
            pass
    #return HttpResponse('<h1>'+str(len(comentarios[0].padre_id))+"  "+str(len(listacomentarios))+'</h1>')
    #return HttpResponse('<h1>'+str(foro.title)+'</h1>')
    if request.method == 'POST':
        #respuesta
        listacomentarios=list()
        if request.POST.get('reply')=="True":

            Coment.objects.create(
                content=request.POST.get("comentario"),
                id_user_id=request.user.id,
                id_forum_id=idforo,
                padre_id=request.POST.get("padre_id"),
            )
            foro=Forums.objects.get(id=idforo)
            comentarios=Coment.objects.filter(id_forum_id=foro.id)
            #codigo para ordenar comentarios poniendo las respuestas debajo del comentario
            for comentario in comentarios:
                if comentario.padre_id==None:
                    comentario.padre_id='None'
                    listacomentarios.append(comentario)
                    for coment in comentarios:
                        if coment.padre_id==comentario.id:
                            listacomentarios.append(coment)
                        else:
                            pass
                else:
                    pass
            time.sleep(1)
            #return redirect(request,idforo=idforo,foro=foro,comments=listacomentarios,userid=userid,username=username)
            return render(request,'comentforo.html',{
                'del_comentario':'False',
                'comentar':'False',
                'reply':'False',
                'foro':foro,
                'comments':listacomentarios,
                'userid':userid,
                "username":username,
            })
            #comentario
        if request.POST.get("comentar")=='True':

            Coment.objects.create(
                content=request.POST.get("comentario"),
                id_user_id=request.user.id,
                id_forum_id=idforo,
            )
            foro=Forums.objects.get(id=idforo)
            comentarios=Coment.objects.filter(id_forum_id=foro.id)
            #codigo para ordenar comentarios poniendo las respuestas debajo del comentario
            for comentario in comentarios:
                if comentario.padre_id==None:
                    comentario.padre_id='None'
                    listacomentarios.append(comentario)
                    for coment in comentarios:
                        if coment.padre_id==comentario.id:
                            listacomentarios.append(coment)
                        else:
                            pass
                else:
                    pass
            time.sleep(1)
            return render(request,'comentforo.html',{
                'comentar':'False',
                'reply':'False',
                'foro':foro,
                'comments':listacomentarios,
                'userid':userid,
                "username":username,
            })
        #eliminar comentario/respuesta        
        if request.POST.get("del_comentario")=='True':
            comentario=Coment.objects.get(id=int(request.POST.get("id_comentario")))
            comentario.delete()
            foro=Forums.objects.get(id=idforo)
            comentarios=Coment.objects.filter(id_forum_id=foro.id)
            #codigo para ordenar comentarios poniendo las respuestas debajo del comentario
            for comentario in comentarios:
                if comentario.padre_id==None:
                    comentario.padre_id='None'
                    listacomentarios.append(comentario)
                    for coment in comentarios:
                        if coment.padre_id==comentario.id:
                            listacomentarios.append(coment)
                        else:
                            pass
                else:
                    pass
            time.sleep(1)
            return render(request,'comentforo.html',{
                'comentar':'False',
                'reply':'False',
                'del_comentario':'False',
                'foro':foro,
                'comments':listacomentarios,
                'userid':userid,
                "username":username,
    })
            #obtengo todos los comentarios de este foro
    #for comentario in comentarios:
    #    if comentario.id_padre
    time.sleep(1)
    return render(request,'comentforo.html',{
        'comentar':'False',
        'reply':'False',
        'del_comentario':'False',
        'foro':foro,
        'comments':listacomentarios,
        'userid':userid,
        "username":username,
    })
