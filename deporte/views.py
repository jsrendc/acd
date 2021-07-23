from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Dep</h1><a href='/deporte/agregar'>agregar</a>")
    
    

def agregar(request):
    return HttpResponse("deporte-Agregar")

