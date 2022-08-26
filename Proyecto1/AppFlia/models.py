from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=100)
    parentesco=models.CharField(max_length=100)
    edad=models.IntegerField()
    cumple=models.DateField()

    


