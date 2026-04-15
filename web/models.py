from django.db import models

class Suelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


from django.db import models


class Suelo(models.Model):

    TIPO_CHOICES = [
        ('arcilloso', 'Arcilloso'),
        ('arenoso', 'Arenoso'),
        ('limoso', 'Limoso'),
        ('franco', 'Franco'),
        ('mixto', 'Mixto'),
        ('organico', 'Orgánico'),
    ]

    PH_CHOICES = [
        ('acido', 'Ácido (< 6.0)'),
        ('neutro', 'Neutro (6.0 - 7.0)'),
        ('alcalino', 'Alcalino (> 7.0)'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, blank=True, null=True)
    ph = models.CharField(max_length=50, choices=PH_CHOICES, blank=True, null=True)
    imagen = models.ImageField(upload_to='suelos/', blank=True, null=True)
    drenaje = models.CharField(max_length=100, blank=True, null=True, help_text="Ej: Bueno, Moderado, Deficiente")
    cultivos_recomendados = models.TextField(blank=True, null=True, help_text="Cultivos que crecen bien en este suelo")

    def __str__(self):
        return self.nombre


class Cultivo(models.Model):

    REGIONES = [
        ('andina', 'Región Andina'),
        ('caribe', 'Región Caribe'),
        ('pacifica', 'Región Pacífica'),
        ('orinoquia', 'Región Orinoquía'),
        ('amazonia', 'Región Amazonía'),
        ('insular', 'Región Insular'),
    ]

    CLIMA_CHOICES = [
        ('calido', 'Cálido'),
        ('templado', 'Templado'),
        ('frio', 'Frío'),
        ('paramo', 'Páramo'),
    ]

    TEMPORADA_CHOICES = [
        ('enero-marzo', 'Enero - Marzo'),
        ('abril-junio', 'Abril - Junio'),
        ('julio-septiembre', 'Julio - Septiembre'),
        ('octubre-diciembre', 'Octubre - Diciembre'),
        ('todo-el-año', 'Todo el año'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cultivos/')
    suelo = models.ForeignKey(Suelo, on_delete=models.CASCADE)
    region = models.CharField(max_length=50, choices=REGIONES, blank=True, null=True)
    clima = models.CharField(max_length=50, choices=CLIMA_CHOICES, blank=True, null=True)
    temporada = models.CharField(max_length=50, choices=TEMPORADA_CHOICES, blank=True, null=True)
    rendimiento_ha = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Toneladas por hectárea")
    altura_minima = models.IntegerField(blank=True, null=True, help_text="Metros sobre el nivel del mar")
    altura_maxima = models.IntegerField(blank=True, null=True, help_text="Metros sobre el nivel del mar")

    def __str__(self):
        return self.nombre


class Cultivo(models.Model):

    REGIONES = [
        ('andina', 'Región Andina'),
        ('caribe', 'Región Caribe'),
        ('pacifica', 'Región Pacífica'),
        ('orinoquia', 'Región Orinoquía'),
        ('amazonia', 'Región Amazonía'),
        ('insular', 'Región Insular'),
    ]

    CLIMA_CHOICES = [
        ('calido', 'Cálido'),
        ('templado', 'Templado'),
        ('frio', 'Frío'),
        ('paramo', 'Páramo'),
    ]

    TEMPORADA_CHOICES = [
        ('enero-marzo', 'Enero - Marzo'),
        ('abril-junio', 'Abril - Junio'),
        ('julio-septiembre', 'Julio - Septiembre'),
        ('octubre-diciembre', 'Octubre - Diciembre'),
        ('todo-el-año', 'Todo el año'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cultivos/')
    suelo = models.ForeignKey(Suelo, on_delete=models.CASCADE)
    region = models.CharField(max_length=50, choices=REGIONES, blank=True, null=True)
    clima = models.CharField(max_length=50, choices=CLIMA_CHOICES, blank=True, null=True)
    temporada = models.CharField(max_length=50, choices=TEMPORADA_CHOICES, blank=True, null=True)
    rendimiento_ha = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, help_text="Toneladas por hectárea")
    altura_minima = models.IntegerField(blank=True, null=True, help_text="Metros sobre el nivel del mar")
    altura_maxima = models.IntegerField(blank=True, null=True, help_text="Metros sobre el nivel del mar")

    def __str__(self):
        return self.nombre
    
    