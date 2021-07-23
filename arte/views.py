from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Arte

# Create your views here.
def agregar(request):
    return HttpResponse("Arte-Agregar")


def inicio(request):
    return HttpResponse("<a href='/arte/agregar'>agregar</a>")



class Lista(generic.ListView):
    model =  Arte
    context_object_name = 'art'
    template_name = "arte.html"