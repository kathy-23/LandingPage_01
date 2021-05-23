from django.shortcuts import render
from django.http import HttpResponse#AGREGADO
# Create your views here.

def index(request): #pasamos un objeto de tipo request como primer argumento
    
    return render(request,'web_colunga/index.html')
    #return HttpResponse(request,'web_colunga/index.html')
    #return render(request,'web_colunga/index.html')
    #return render(request,'index.html')
    #return render(request,'Template/index.html')
    #return render(request,'Template/web_colunga/index.html')


    #login
    #main