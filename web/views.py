from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def cultivos(request):
    return render(request, 'cultivos.html')

def suelos(request):
    return render(request, 'suelos.html')

def galeria(request):
    return render(request, 'galeria.html')

def dashboard(request):
    return render(request, 'dashboard.html') 


from django.shortcuts import render
from .models import Cultivo

def cultivos(request):

    busqueda = request.GET.get("buscar")

    if busqueda:
        cultivos = Cultivo.objects.filter(nombre__icontains=busqueda)
    else:
        cultivos = Cultivo.objects.all()

    return render(request, "cultivos.html", {
        "cultivos": cultivos
    })


from .models import Cultivo, Suelo

def cultivos(request):

    busqueda = request.GET.get("buscar")
    suelo_id = request.GET.get("suelo")

    cultivos = Cultivo.objects.all()

    if busqueda:
        cultivos = cultivos.filter(nombre__icontains=busqueda)

    if suelo_id:
        cultivos = cultivos.filter(suelo_id=suelo_id)

    suelos = Suelo.objects.all()

    return render(request, "cultivos.html", {
        "cultivos": cultivos,
        "suelos": suelos
    })


def dashboard(request):

    total_cultivos = Cultivo.objects.count()
    total_suelos = Suelo.objects.count()

    return render(request, "dashboard.html", {
        "total_cultivos": total_cultivos,
        "total_suelos": total_suelos
    })


def galeria(request):

    cultivos = Cultivo.objects.all()

    return render(request, "galeria.html", {
        "cultivos": cultivos
    })