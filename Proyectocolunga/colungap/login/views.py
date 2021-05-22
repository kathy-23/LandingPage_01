from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
def ingreso(request,redir=""):
    if request.method == "POST":
        email=request.POST['txt_mail']
        password=request.POST['txt_password']
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff==True or user.is_superuser==True:
                return redirect('addUser')
            else:
                return redirect('inicio')
        else:
            messages.info(request,'Credenciales invalidas,porfavor ingresa tus credenciales nuevamente')

    elif redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    return render(request,'ingreso.html')