from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages


def comentforo(request,redir=''):
    
    
    
    if redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    return HttpResponse('<h1>a</h1>')



def listforo(request,redir=''):


    
    if redir=='main.html':
        return redirect('main')
    elif redir=='addUser.html':
        return redirect('addUser')
    elif redir=='inicio.html':
        return redirect('inicio')
    elif redir=='ingreso.html':
        return redirect('ingreso')
    return HttpResponse('<h1>a</h1>')