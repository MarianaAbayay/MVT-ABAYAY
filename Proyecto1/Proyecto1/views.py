#CONTROLADOR

from django import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenidxs")

def familiares(request):
    return HttpResponse("FAMILIARES")
    