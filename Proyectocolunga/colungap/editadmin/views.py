from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect, render, HttpResponse
from .forms import AddUserForm,EditUserForm
from .models import Miembro
'''
la forma de agregar y usuarios cambio ya que si se remueve a un usuario de la bdd y luego se vuelve agregar, su id cambiaria
y si anteriormente ese usuario eliminado hizo alguna publicacion en el foro iban a existir conflictos por id
quizas mostraba que cierto comentario lo hizo x persona cuando en realidad no fue asi
asi que la eliminacion de usuario ahora en realidad no lo elimina de la bdd sino que deja al usuario inactivo 
en la linea 115 y 69 se puede ver esto ya que los datos que obtengo para mostrar en la lista poseen una excepcion de si el usuario esta activo o no
'''


def addUser(request,redir=''):
    usuario=User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    #obtiene por POST la informacion del formulario
    adduserform = AddUserForm(request.POST)
    #consulto si el metodo es POST 
    if request.method == 'POST':
        if request.POST.get("btn_logout")=="logout":
            logout(request)
            return redirect('main')
        #almaceno el email del formulario
        email=request.POST.get('email')
        
        #creo un objeto usuario con el email que recibi del formulario
        try:
            usuario=User.objects.get(email=email) 
        except:
            usuario=None
        #return HttpResponse('<h1>'+usuario+'</h1>')
        #pregunto si el objeto creado contiene datos
        if usuario is not None:
            #pregunto si el llenaod de formulario es valido (todos los campos llenados y password con mayusculas y minusculas y minimo 8 caracteres)
            #el correo registrado ya existe en la base de datos, preguntar si desea sobreescribir o usar el existente?
            # opcion sobreescribir
            '''if adduserform.is_valid():
                    adduserform.save()
                    return redirect('addUser')'''
            #usar existente
            usuario.is_active=True
            usuario.save()
            return render(request,'addUser.html',{
                'addUserform':adduserform,
                'username':username
            })
        #si el usuario no existe
        else:
            #valido el formulario
            
            if adduserform.is_valid():
                #guardo los datos del formulario
                adduserform.save()
                """
                usuario=User.objects.create(
                    username=request.POST.get('email'),
                    email=request.POST.get('email'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    password=adduserform.cleaned_data['password1']
                )
                usuario.save()
                """
                return render(request,'addUser.html',{
                    'addUserform':adduserform,
                    'username':username
                })
            else:
                print(adduserform.is_valid())
                return HttpResponse('<h1>no se pudo agregar el usuario'+str(adduserform)+'</h1>')
        
    if redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='removeUser.html':
        return redirect('removeUser')
    elif redir=='editUser.html':
        return redirect('editUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    elif redir=='logout':
        logout(request)
        return redirect('main')

    return render(request,'addUser.html',{
        'addUserform':adduserform,
        'username':username
    })



def removeUser(request,redir=''):
    usuario=User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    #multiples obejetos con la inf de los usuarios
    usuarios=User.objects.exclude(is_active=False).all()
    #return HttpResponse('<h1>'+str(usuarios)+'</h1>')
    #cantidad de usuarios a mostrar en la lista
    cant_user="size="+str(len(usuarios))
    
    #accion de eliminar un usuario
    if request.method =='POST':
        if request.POST.get("btn_logout")=="logout":
            logout(request)
            return redirect('main')
        #obtiene lo enviado por la pagina
        email=request.POST.get('user_list')
        #crea el objeto de la tabla que contiene ese email
        remov = User.objects.get(email=email)
        if remov is not None:#si encontro al usuario 'not none'
            remov.is_active=False #borrar en la tabla a lo que corresponde el objeto
            remov.save()
            usuarios=User.objects.exclude(is_active=False).all()
            #return HttpResponse('<h1>'+str(remov)+'</h1>')
            return render(request,'removeUser.html',{
                'username':username,
                'list_user':usuarios,
                'cant_user':cant_user,
            })#redirecciona a la misma pagina
        else:
            pass
    
    
    elif redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='removeUser.html':
        return redirect('removeUser')
    elif redir=='editUser.html':
        return redirect('editUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    elif redir=='logout':
        logout(request)
        return redirect('main')
    else: pass

    return render(request,'removeUser.html',{
        'username':username,
        'list_user':usuarios,
        'cant_user':cant_user,
    })



def editUser(request,redir=''):
    usuario=User.objects.get(id=request.user.id)
    username=usuario.first_name+" "+usuario.last_name
    usuarios=User.objects.exclude(is_active=False).all()
    cant_user="size="+str(len(usuarios))
    if request.method == 'POST':
        if request.POST.get("btn_logout")=="logout":
            logout(request)
            return redirect('main')
        save=str(request.POST.get('save'))
        showform=str(request.POST.get('showform'))
        if(showform=='True'):
            email=str(request.POST.get('email'))
            
            usuario=User.objects.get(email=email)
            miembro=Miembro.objects.get(user_id=usuario.id)
            editUserform=EditUserForm(initial={
                'first_name':usuario.first_name,
                'last_name':usuario.last_name,
                'email':usuario.email,
                'telefono':miembro.telefono,
                'cargo':miembro.cargo,
                'organizacion':miembro.organizacion,
                'password':""
            })
            #return HttpResponse('<h1>'+usuario.first_name+usuario.last_name+usuario.email+'</h1>')
            return render(request,'editUser.html',{
                'username':username,
                'editUserform':editUserform,
                'showform':'True',
                'user_list': usuarios,
                'cant_user': cant_user,
                'selectedemail':email,
            })

        elif(showform=='False' and save=='True'):
            selectedemail=request.POST.get('selectedemail')
            formuser=EditUserForm(request.POST)
            usuario=User.objects.get(email=selectedemail)
            miembro=Miembro.objects.get(user_id=usuario.id)
            password=request.POST.get('password1')
            #return HttpResponse('<h1>'+str(usuario.first_name)+usuario.last_name+usuario.email+'</h1>')
            if request.POST.get('password1')!='':
                usuario.first_name=formuser.data.get('first_name')
                usuario.last_name=formuser.data.get('last_name')
                usuario.email=formuser.data.get('email')
                usuario.set_password(password)
                miembro.id_user=usuario.id
                miembro.telefono=formuser.data.get('telefono')
                miembro.organizacion=formuser.data.get('organizacion')
                miembro.cargo=formuser.data.get('cargo')
                usuario.save()
                miembro.save()
                print("aqui1")
                usuarios=User.objects.exclude(is_active=False).all()
                return render(request,'editUser.html',{
                    'username':username,
                    'showform':'False',
                    'save':'False',
                    'user_list': usuarios,
                    'cant_user': cant_user,
                })
            else:
                usuario.first_name=formuser.data.get('first_name')
                usuario.last_name=formuser.data.get('last_name')
                usuario.email=formuser.data.get('email')
                usuario.save()
                print("aqui2")
                usuarios=User.objects.exclude(is_active=False).all()
                return render(request,'editUser.html',{
                    'username':username,
                    'showform':'False',
                    'save':'False',
                    'user_list': usuarios,
                    'cant_user': cant_user,
                })
                

    elif redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='removeUser.html':
        return redirect('removeUser')
    elif redir=='editUser.html':
        return redirect('editUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    elif redir=='logout':
        logout(request)
        return redirect('main')

    return render(request,'editUser.html',{
        'username':username,
        'showform':'False',
        'save' : 'False',
        'user_list': usuarios,
        'cant_user': cant_user,
    })
# Create your views here.
