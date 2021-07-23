from django import forms
from .models import Arte


class FormularioRegistro(forms.ModelForm):
    class Meta:
        model  =  Arte
        fields = ["nombre","descripcion"]
        
