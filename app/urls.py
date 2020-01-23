from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index),
    path('iniciosesion/', views.iniciosesion),
    path('cerrarsesion/', views.cerrarsesion),
    path('aspirante/', views.aspirante),
    path('alumno/', views.alumno),
    path('crear_usuario/', views.crear_usuario),
    path('recu_passw/', views.recu),
    #nuevas vistas
    path('k/', views.k),
    path('intereses/', views.test),
    path('lista/', views.lista),
    path('perfil/', views.perfil),
    path('resultado/', views.resultado),
    path('aptitudes/', views.test),
    path('test/', views.testuno),
    
    
]
