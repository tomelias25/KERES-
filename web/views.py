from django.shortcuts import render
from .models import Cultivo, Suelo


def inicio(request):
    return render(request, 'inicio.html')


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


def suelos(request):
    suelos = Suelo.objects.all()

    return render(request, "suelos.html", {
        "suelos": suelos
    })


def galeria(request):

    cultivos = Cultivo.objects.all()

    return render(request, "galeria.html", {
        "cultivos": cultivos
    })


def dashboard(request):

    total_cultivos = Cultivo.objects.count()
    total_suelos = Suelo.objects.count()

    return render(request, "dashboard.html", {
        "total_cultivos": total_cultivos,
        "total_suelos": total_suelos
    })