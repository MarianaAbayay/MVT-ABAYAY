from django.shortcuts import render
from http.client import HTTPResponse
from .models import Familiar

def familiar1(request):
    familiar1= Familiar(nombre= "Paula", parentesco="hermana", edad=45, cumple=15/8)
    familiar1.save()
    texto= f"Familiar agregado: Su nombre es {familiar1.nombre} y el parentesco que guarda es el de {familiar1.parentesco}. La fecha de su cumpleaños es {familiar1.cumple}, actualmente tiene {familiar1.edad} años de edad."
    return HTTPResponse(texto)

def familiar2(request):
    familiar2= Familiar(nombre= "Aldana", parentesco="hermana", edad=24, cumple=11/3)
    familiar2.save()
    texto= f"Familiar agregado: Su nombre es {familiar2.nombre} y el parentesco que guarda es el de {familiar2.parentesco}. La fecha de su cumpleaños es {familiar2.cumple}, actualmente tiene {familiar2.edad} años de edad."
    return HTTPResponse(texto)

def familiar3(request):
    familiar3= Familiar(nombre= "Gonzalo", parentesco="primo", edad=36, cumple=16/10)
    familiar3.save()
    texto= f"Familiar agregado: Su nombre es {familiar3.nombre} y el parentesco que guarda es el de {familiar3.parentesco}. La fecha de su cumpleaños es {familiar3.cumple}, actualmente tiene {familiar3.edad} años de edad."
    return HTTPResponse(texto)