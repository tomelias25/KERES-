# Importa la función para renderizar plantillas HTML
from django.shortcuts import render

# Importa los modelos Cultivo y Suelo de la base de datos
from .models import Cultivo, Suelo


# Vista principal (inicio)
def inicio(request):
    # Obtiene todos los registros de cultivos
    cultivos = Cultivo.objects.all()
    
    # Renderiza la plantilla inicio.html enviando los cultivos
    return render(request, 'inicio.html', {'cultivos': cultivos})


# Vista de lista de cultivos con filtros
def cultivos(request):
    # Obtiene el texto de búsqueda desde la URL (?buscar=...)
    busqueda = request.GET.get("buscar")
    
    # Obtiene el id del suelo desde la URL (?suelo=...)
    suelo_id = request.GET.get("suelo")

    # Trae todos los cultivos inicialmente
    cultivos = Cultivo.objects.all()

    # Si hay búsqueda, filtra por nombre (no sensible a mayúsculas)
    if busqueda:
        cultivos = cultivos.filter(nombre__icontains=busqueda)

    # Si hay filtro por suelo, filtra por ese id
    if suelo_id:
        cultivos = cultivos.filter(suelo_id=suelo_id)

    # Obtiene todos los suelos para mostrarlos en filtros
    suelos = Suelo.objects.all()

    # Renderiza la plantilla con cultivos y suelos
    return render(request, "cultivos.html", {
        "cultivos": cultivos,
        "suelos": suelos
    })


# Vista para listar todos los suelos
def suelos(request):
    # Obtiene todos los suelos
    suelos = Suelo.objects.all()
    
    # Renderiza la plantilla suelos.html
    return render(request, "suelos.html", {"suelos": suelos})


# Vista de galería de cultivos
def galeria(request):
    # Obtiene todos los cultivos
    cultivos = Cultivo.objects.all()
    
    # Renderiza la galería
    return render(request, "galeria.html", {"cultivos": cultivos})


# Vista de productividad (simple)
def Productividad(request):
    # Renderiza la plantilla con totales básicos
    return render(request, "productividad.html", {
        "total_cultivos": Cultivo.objects.count(),  # Cuenta cultivos
        "total_suelos": Suelo.objects.count()       # Cuenta suelos
    })


# Importa función para obtener objetos o error 404
from django.shortcuts import render, get_object_or_404

# Importa nuevamente los modelos (redundante, ya estaban arriba)
from .models import Cultivo, Suelo


# Vista inicio repetida (duplicada)
def inicio(request):
    cultivos = Cultivo.objects.all()
    return render(request, 'inicio.html', {'cultivos': cultivos})


# Vista cultivos repetida (duplicada)
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


# Vista detalle de un cultivo específico
def detalle_cultivo(request, cultivo_id):
    # Busca el cultivo por id o devuelve error 404 si no existe
    cultivo = get_object_or_404(Cultivo, id=cultivo_id)
    
    # Obtiene cultivos del mismo suelo (excepto el actual)
    cultivos_relacionados = Cultivo.objects.filter(
        suelo=cultivo.suelo
    ).exclude(id=cultivo_id)[:3]  # Limita a 3 resultados

    # Renderiza la vista detalle
    return render(request, "detalle_cultivo.html", {
        "cultivo": cultivo,
        "relacionados": cultivos_relacionados
    })


# Vista suelos repetida (duplicada)
def suelos(request):
    suelos = Suelo.objects.all()
    return render(request, "suelos.html", {"suelos": suelos})


# Vista galería repetida (duplicada)
def galeria(request):
    cultivos = Cultivo.objects.all()
    return render(request, "galeria.html", {"cultivos": cultivos})


# Vista productividad repetida (sobrescrita luego)
def Productividad(request):
    return render(request, "productividad.html", {
        "total_cultivos": Cultivo.objects.count(),
        "total_suelos": Suelo.objects.count()
    })


# Vista detalle de un suelo
def detalle_suelo(request, suelo_id):
    # Busca el suelo por id o devuelve 404
    suelo = get_object_or_404(Suelo, id=suelo_id)
    
    # Obtiene los cultivos asociados a ese suelo
    cultivos = Cultivo.objects.filter(suelo=suelo)

    # Renderiza la vista detalle del suelo
    return render(request, "detalle_suelo.html", {
        "suelo": suelo,
        "cultivos": cultivos
    })


# Importa funciones para agregaciones (conteo y promedio)
from django.db.models import Count, Avg


# Vista productividad avanzada (esta reemplaza las anteriores)
def Productividad(request):
    # Cuenta total de cultivos
    total_cultivos = Cultivo.objects.count()
    
    # Cuenta total de suelos
    total_suelos = Suelo.objects.count()

    # Agrupa cultivos por región y cuenta cuantos hay
    cultivos_por_region = list(
        Cultivo.objects.exclude(region=None)
        .values('region')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Agrupa cultivos por tipo de suelo
    cultivos_por_suelo = list(
        Cultivo.objects.values('suelo__nombre')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Agrupa cultivos por clima
    cultivos_por_clima = list(
        Cultivo.objects.exclude(clima=None)
        .values('clima')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Obtiene los 6 cultivos con mejor rendimiento por hectárea
    top_rendimiento = list(
        Cultivo.objects.exclude(rendimiento_ha=None)
        .values('nombre', 'rendimiento_ha')
        .order_by('-rendimiento_ha')[:6]
    )

    # Renderiza la vista con todos los datos
    return render(request, "productividad.html", {
        "total_cultivos": total_cultivos,
        "total_suelos": total_suelos,
        "cultivos_por_region": cultivos_por_region,
        "cultivos_por_suelo": cultivos_por_suelo,
        "cultivos_por_clima": cultivos_por_clima,
        "top_rendimiento": top_rendimiento,
    })