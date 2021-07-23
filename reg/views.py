from django.shortcuts import render,redirect

from reg.fr import FormularioRegistro

# Create your views here.

"""
def registro(request):
    frm = FormularioRegistro()

    if request.method == "POST":
        frm = FormularioRegistro(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect("/")

    return render(request,"registro.html", {"formularioR": frm})
"""

def registro(request):
    frm = FormularioRegistro()

    if request.method == "POST":
        frm = FormularioRegistro(request.POST)
        print(frm)
        """
        frm.act = 1
        f2 = frm.save(commit=False)
        f2.act = 1
        if f2.is_valid():
            f2.save()
            return redirect("/")
        """

    return render(request,"registro.html", {"formularioR": frm})
    
