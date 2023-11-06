from django.db import models

# Create your models here.

class Paciente(models.Model):
        codigo = models.CharField(primary_key=True, max_length=13)
        nombre = models.CharField(max_length=50)
        sexo = models.CharField(max_length=8)

        def __str__(self): 
                texto = "{0} ({1})"
                return texto.format(self.nombre, self.sexo)

class Empleados(models.Model):
        codigo = models.CharField(primary_key=True, max_length=13)
        nombre = models.CharField(max_length=50)
        sexo = models.CharField(max_length=8)
        edad = models.CharField(max_length=3)
        profesion=models.CharField(max_length=50)

        def __str__(self): 
                texto = "{0} ({3})"
                return texto.format(self.nombre, self.sexo, self.edad, self.profesion)

class Consultas(models.Model):
        codigo = models.CharField(primary_key=True, max_length=13)
        nombre = models.CharField(max_length=50)
        sexo = models.CharField(max_length=8)
        edad = models.CharField(max_length=3)
        especialidad = models.CharField(max_length=50)
        motivo = models.CharField(max_length=100)

        def __str__(self): 
                texto = "{0} ({4})"
                return texto.format(self.nombre, self.sexo, self.edad, self.especialidad, self.motivo)