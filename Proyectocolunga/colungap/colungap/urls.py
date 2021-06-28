"""colungap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views as main
from login import views as login
from inicio import views as inicio
from editadmin import views as editadmin
from forums import views as forum
from anuncios import views as anuncio
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
                        
    path('main/',main.main,name='main'),
    path('main/<str:redir>',main.main,name='main'),
                                
    path('ingreso/',login.ingreso,name='ingreso'),
    path('ingreso/<str:redir>',login.ingreso,name='ingreso'),
                              
    path('addUser/',editadmin.addUser,name='addUser'),
    path('addUser/<str:redir>',editadmin.addUser,name='addUser'),
    path('removeUser/',editadmin.removeUser,name='removeUser'),
    path('removeUser/<str:redir>',editadmin.removeUser,name='removeUser'),
    path('editUser/',editadmin.editUser,name='editUser'),
    path('editUser/<str:redir>',editadmin.editUser,name='editUser'),
                                            
    path('inicio/',inicio.inicio,name='inicio'),     
    path('inicio/<str:redir>',inicio.inicio,name='inicio'),  

    path('inicioAnuncios/',anuncio.addAnuncio,name='inicio_anuncios'),     
    path('inicioAnuncios/<str:redir>',anuncio.addAnuncio,name='inicio_anuncios'),    
    
    path('inicioTopicos/',forum.inicio_topicos,name='inicio_topicos'),     
    path('inicioTopicos/<str:redir>',forum.inicio_topicos,name='inicio_topicos'),         
                                          
    path('comentforo',forum.comentforo,name='comentforo'),
    path('comentforo/<str:idforo>',forum.comentforo,name='comentforo'),
    path('colungahub/',inicio.hub,name='hub'),
    path('colungahub/<str:redir>',inicio.hub,name='hub'),
    #olvide contraseña-------------vistas
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name ="password_reset1.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset2.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name ="password_reset3.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name ="password_reset4.html"),name="password_reset_complete"),
]