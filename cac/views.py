from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando se accede por GET'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    parameters_get = request.GET.get('otro')
    return HttpResponse(f"""
        <h1>{titulo}</h1>
        <p>{parameters_get}</p>
    """)


def hola_mundo(request):
    return HttpResponse('Hola mundo Django')

def saludar(request,nombre):
    return HttpResponse(f"""
        <h1>Hola Mundo - {nombre}</h1>
        <p>Esto es una prueba</p>
    """)
    
def cursos_detalle(request,nombre_curso):
    return HttpResponse(f"""
        <h1>{nombre_curso}</h1>
    """)


def cursos(request,nombre):
    return HttpResponse(f"""
        <h2>{nombre}</h2>
    """)