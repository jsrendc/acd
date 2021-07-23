from django.db import models

# Create your models here.
class Arte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    tipo = models.CharField(choices=[("B","Baile"),("M","Música")],max_length=2)

    def get_nombre(self):
        return self.nombre

class Baile(models.Model):
    reg = models.CharField(max_length=20)
