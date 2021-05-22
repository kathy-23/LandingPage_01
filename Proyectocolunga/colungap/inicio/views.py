from django.shortcuts import render, redirect






def inicio(request,redir=""):
    if redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    return render(request,'inicio.html')
# Create your views here.
