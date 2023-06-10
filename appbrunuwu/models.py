from django.db import models

class Clase1(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.TextField()

class Clase2(models.Model):
    campo3 = models.IntegerField()
    campo4 = models.DateField()

class Clase3(models.Model):
    campo5 = models.CharField(max_length=100)
    campo6 = models.EmailField()


#ARREGLAR MODELS.PY FORMS.PY VIEWS.PY 
# CREAR CLASES ACORDES 
# Hacer un html mas bonito con su css, en teoria ya esta listo para usar
