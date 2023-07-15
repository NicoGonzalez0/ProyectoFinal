from django.http import HttpResponse
from django.template import loader

#Creacion de vistas

def saludo(request):
    return("Hola mundo")

def inicio(request):
    return("Vista Inicio")

def Funciones(request):
    return("Vista Funciones")
