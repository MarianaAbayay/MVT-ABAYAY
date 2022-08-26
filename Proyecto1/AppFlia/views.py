from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import HttpResponse
from .models import Familiar

def familiar1(request):
    familiar1= Familiar(nombre= "Paula", parentesco="hermana", edad="45", cumple= "1976/8/15")
    familiar1.save()
    texto= f"Familiar agregado: Su nombre es {familiar1.nombre} y el parentesco que guarda es el de {familiar1.parentesco}. La fecha de su cumpleaños es {familiar1.cumple}, actualmente tiene {familiar1.edad} años de edad."
    return HttpResponse(texto)

def familiar2(request):
    familiar2= Familiar(nombre= "Aldana", parentesco="hermana", edad=24, cumple="1998/03/11")
    familiar2.save()
    texto= f"Familiar agregado: Su nombre es {familiar2.nombre} y el parentesco que guarda es el de {familiar2.parentesco}. La fecha de su cumpleaños es {familiar2.cumple}, actualmente tiene {familiar2.edad} años de edad."
    return HttpResponse(texto)

def familiar3(request):
    familiar3= Familiar(nombre= "Gonzalo", parentesco="primo", edad="36", cumple="1986/10/16")
    familiar3.save()
    texto= f"Familiar agregado: Su nombre es {familiar3.nombre} y el parentesco que guarda es el de {familiar3.parentesco}. La fecha de su cumpleaños es {familiar3.cumple}, actualmente tiene {familiar3.edad} años de edad."
    return HttpResponse(texto)