from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.core import serializers
from django.contrib.auth.hashers import check_password
import json
import smtplib
import sweetify
import datetime

# Create your views here.


def index(request):
    usuario = request.user
    if usuario.is_active:
        return render (request, 'index.html', {})
    else:
        return render(request, 'login.html',{})



# LOGIN Y CERRAR SESION
def iniciosesion(request):
    username = request.POST.get("usuario")
    password = request.POST.get("password")
    print("Esto llego: ", username)
    try: 
        username = authenticate(request, username=username, password=password)
        login(request,username)
        return redirect('/')
    except Exception as e:
        sweetify.error(request, 'Oops!', text='¡El Usuario y/o Contraseña es Incorrecto!', persistent=':´(')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def cerrarsesion(request):
	logout(request)
	return HttpResponseRedirect("/")

def recu(request):
    return render(request, "recu.html", {})
def aspirante(request):
    return render(request, "aspirante.html", {})

def alumno(request):
    return render(request, "alumno.html", {})
#<!--nuevas vistas-->    
def test(request):
    return render(request, "test.html", {})

def testuno(request):
    return render(request, "testuno.html", {})

def perfil(request):
    return render(request, "perfil.html", {})

def lista(request):
    return render(request, "lista.html", {})

def resultado(request):
    return render(request, "resultado.html", {})





def k(request):
    return render(request, "login.html", {})

@csrf_exempt
def crear_usuario(request):
    tipo =  request.POST.get("tipo")
    print("Recibiendo el tipo: ", tipo)

    nombre =  request.POST.get("nombre")
    apellidos = request.POST.get("apellidos")
    usuario = request.POST.get("usuario")
    password = request.POST.get("password")
    correo = request.POST.get("correo")

    edad = request.POST.get("edad")
    sexo = request.POST.get("sexo")

    if tipo == "Aspirante":
        
        preparatoria= request.POST.get("preparatoria")
        direccion = request.POST.get("direccion")
        promedio = request.POST.get("promedio")
        area = request.POST.get("area")

        user = User.objects.filter(username=usuario).exists()
        if user == False:
            user = User.objects.create_user(first_name=nombre,
            last_name = apellidos,
            email = correo,
            username = usuario,
            password = password)

            aspirante = Usuarios.objects.create(usuario=user, tipo=tipo, edad=edad, sexo=sexo,
            preparatoria=preparatoria, direccion=direccion, promedio=promedio, area=area)

            print("Usuario creado con exito")

            user = authenticate(request, username=usuario, password=password)

            

            # user = authenticate(request, username=usuario, password=password)
    
    if tipo == "Alumno":
        no_control = request.POST.get("control")
        password = request.POST.get("password")
        semestre = request.POST.get("semestre")

        user = User.objects.filter(username=usuario).exists()
        if user == False:
            user = User.objects.create_user(first_name=nombre,
            last_name = apellidos,
            email = correo,
            username = usuario,
            password = password)

            alumno = Usuarios.objects.create(usuario=user, tipo=tipo, edad=edad, sexo=sexo,
            no_control=no_control, password=password, semestre=semestre)

            print("Usuario creado con exito")

            user = authenticate(request, username=usuario, password=password)

        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
