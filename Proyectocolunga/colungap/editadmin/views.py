from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect, render, HttpResponse
from .forms import AddUserForm, EditUserForm
'''
la forma de agregar y usuarios cambio ya que si se remueve a un usuario de la bdd y luego se vuelve agregar, su id cambiaria
y si anteriormente ese usuario eliminado hizo alguna publicacion en el foro iban a existir conflictos por id
quizas mostraba que cierto comentario lo hizo x persona cuando en realidad no fue asi
asi que la eliminacion de usuario ahora en realidad no lo elimina de la bdd sino que deja al usuario inactivo 
en la linea 115 y 69 se puede ver esto ya que los datos que obtengo para mostrar en la lista poseen una excepcion de si el usuario esta activo o no
'''


def addUser(request,redir=''):
    #obtiene por POST la informacion del formulario
    adduserform = AddUserForm(request.POST)
    #consulto si el metodo es POST 
    if request.method == 'POST':
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
            return redirect('addUser')
        #si el usuario no existe
        else:
            #valido el formulario
            if adduserform.is_valid():
                #guardo los datos del formulario
                usuario=User.objects.create(
                    username='',
                    email=request.POST.get('email'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    password=hash(request.POST.get('password')),
                )
                usuario.save()
                return redirect('addUser')
            else:
                return HttpResponse('<h1>no se pudo agregar el usuario</h1>')
        
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
    })



def removeUser(request,redir=''):
    #multiples obejetos con la inf de los usuarios
    usuarios=User.objects.exclude(is_active=False).all()
    #return HttpResponse('<h1>'+str(usuarios)+'</h1>')
    #cantidad de usuarios a mostrar en la lista
    cant_user="size="+str(len(usuarios))
    
    #accion de eliminar un usuario
    if request.method =='POST':
        #obtiene lo enviado por la pagina
        email=request.POST.get('user_list')
        #crea el objeto de la tabla que contiene ese email
        remov = User.objects.get(email=email)
        if remov is not None:#si encontro al usuario 'not none'
            remov.is_active=False #borrar en la tabla a lo que corresponde el objeto
            remov.save()
            #return HttpResponse('<h1>'+str(remov)+'</h1>')
            return redirect('removeUser')#redirecciona a la misma pagina
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
        'list_user':usuarios,
        'cant_user':cant_user,
    })



def editUser(request,redir=''):

    usuarios=User.objects.exclude(is_active=False).all()
    cant_user="size="+str(len(usuarios))
    if request.method == 'POST':
        save=str(request.POST.get('save'))
        showform=str(request.POST.get('showform'))
        email=str(request.POST.get('email'))
        
        if(showform=='True'):
            usuario=User.objects.get(email=email)
            editUserform=EditUserForm(initial={
                'first_name':usuario.first_name,
                'last_name':usuario.last_name,
                'email':usuario.email,
            })
            #return HttpResponse('<h1>'+usuario.first_name+usuario.last_name+usuario.email+'</h1>')
            return render(request,'editUser.html',{
                'editUserform':editUserform,
                'showform':'True',
                'user_list': usuarios,
                'cant_user': cant_user,
            })
        elif(showform=='False' and save=='True'):
            usuario=User.objects.get(email=email)            
            password=str(request.POST.get('password'))
            usuario.first_name=request.POST.get('first_name')
            usuario.last_name=request.POST.get('last_name')
            usuario.email=request.POST.get('email')
            #return HttpResponse('<h1>'+str(usuario.first_name)+usuario.last_name+usuario.email+'</h1>')
            if password=='':
                usuario.save()
                usuarios=User.objects.exclude(is_active=False).all()
                return render(request,'editUser.html',{
                    'showform':'False',
                    'save':'False',
                    'user_list': usuarios,
                    'cant_user': cant_user,
                })
            else:
                usuario.set_password(request.POST.get('password'))
                usuario.save()
                usuarios=User.objects.exclude(is_active=False).all()
                return render(request,'editUser.html',{
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
        'showform':'False',
        'save' : 'False',
        'user_list': usuarios,
        'cant_user': cant_user,
    })
# Create your views here.
