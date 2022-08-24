#CONTROLADOR

from django import HttpResponse
from django.template import Context, Template


def inicio(request):
    return HttpResponse("Bienvenidxs")

def familiares(request):
    mihtml=open("Proyecto1/Plantillas/template1.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
    