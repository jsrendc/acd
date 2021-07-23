from django import forms
from django.forms import ModelChoiceField

from reg.models import Persona
from arte.models import Arte

class ActArte(ModelChoiceField):
    
    #def valoresArte(self,o):
    def label_from_instance(self,o):
        #return "{0} ".format(o.nombre)#"{0} {1}".format(obj.id,obj.nombre)
        return o.get_nombre()


class FormularioRegistro(forms.ModelForm):
    #nombre = forms.CharField(required=False)
    #correo = forms.CharField(required=False)
    #act = ActArte(Arte.objects.all()) #forms.ChoiceField()
    act = ActArte(Arte.objects.all()) #forms.ChoiceField()

    #tipo = forms.ChoiceField(choices=[("Arte y cultura","Arte y cultuta"),("Deporte","Deporte")])
    tipo = forms.ChoiceField(choices=[("","--Seleccione--"),("AC","A"),("D","D"),])
    class Meta:
        model  =  Persona
        fields = ["nombre","apellidos","sexo","act","tipo"]
        #labels = {"act":"Actividad"}
        widgets={"sexo":forms.RadioSelect, "act":forms.NumberInput()}  



