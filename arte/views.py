from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .fr import FormularioRegistro
from .models import Arte

# Create your views here.
def inicio(request):
    
    return render(request,"arte.html")
    #return HttpResponse("<a href='/arte/agregar'>agregar</a>")


def agregar(request):
    frm = FormularioRegistro()
     
    if request.method == "POST":
        frm = FormularioRegistro(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect("/")
    return render(request,"arte.html", {"formularioR": frm})
    #return HttpResponse("Arte-Agregar")


class Lista(generic.ListView):
    model =  Arte
    context_object_name = 'art'
    template_name = "arte.html"