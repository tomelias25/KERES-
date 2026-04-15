from django.shortcuts import render
from .models import Cultivo, Suelo


def inicio(request):
    cultivos = Cultivo.objects.all()
    return render(request, 'inicio.html', {'cultivos': cultivos})


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
    return render(request, "suelos.html", {"suelos": suelos})


def galeria(request):
    cultivos = Cultivo.objects.all()
    return render(request, "galeria.html", {"cultivos": cultivos})


def Productividad(request):
    return render(request, "productividad.html", {
        "total_cultivos": Cultivo.objects.count(),
        "total_suelos": Suelo.objects.count()
    })

from django.shortcuts import render, get_object_or_404
from .models import Cultivo, Suelo


def inicio(request):
    cultivos = Cultivo.objects.all()
    return render(request, 'inicio.html', {'cultivos': cultivos})


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


def detalle_cultivo(request, cultivo_id):
    cultivo = get_object_or_404(Cultivo, id=cultivo_id)
    cultivos_relacionados = Cultivo.objects.filter(suelo=cultivo.suelo).exclude(id=cultivo_id)[:3]
    return render(request, "detalle_cultivo.html", {
        "cultivo": cultivo,
        "relacionados": cultivos_relacionados
    })


def suelos(request):
    suelos = Suelo.objects.all()
    return render(request, "suelos.html", {"suelos": suelos})


def galeria(request):
    cultivos = Cultivo.objects.all()
    return render(request, "galeria.html", {"cultivos": cultivos})


def Productividad(request):
    return render(request, "productividad.html", {
        "total_cultivos": Cultivo.objects.count(),
        "total_suelos": Suelo.objects.count()
    })

def detalle_suelo(request, suelo_id):
    suelo = get_object_or_404(Suelo, id=suelo_id)
    cultivos = Cultivo.objects.filter(suelo=suelo)
    return render(request, "detalle_suelo.html", {
        "suelo": suelo,
        "cultivos": cultivos
    })

from django.db.models import Count, Avg

def Productividad(request):
    # Datos dinámicos desde la BD
    total_cultivos = Cultivo.objects.count()
    total_suelos = Suelo.objects.count()

    # Cultivos por región
    cultivos_por_region = list(
        Cultivo.objects.exclude(region=None)
        .values('region')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Cultivos por suelo
    cultivos_por_suelo = list(
        Cultivo.objects.values('suelo__nombre')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Cultivos por clima
    cultivos_por_clima = list(
        Cultivo.objects.exclude(clima=None)
        .values('clima')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Rendimiento promedio por cultivo (top 6)
    top_rendimiento = list(
        Cultivo.objects.exclude(rendimiento_ha=None)
        .values('nombre', 'rendimiento_ha')
        .order_by('-rendimiento_ha')[:6]
    )

    return render(request, "productividad.html", {
        "total_cultivos": total_cultivos,
        "total_suelos": total_suelos,
        "cultivos_por_region": cultivos_por_region,
        "cultivos_por_suelo": cultivos_por_suelo,
        "cultivos_por_clima": cultivos_por_clima,
        "top_rendimiento": top_rendimiento,
    })