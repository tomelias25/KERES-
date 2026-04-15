from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cultivos/', views.cultivos, name='cultivos'),
    path('suelos/', views.suelos, name='suelos'),
    path('galeria/', views.galeria, name='galeria'),
    path('productividad/', views.Productividad, name='productividad'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cultivos/', views.cultivos, name='cultivos'),
    path('cultivos/<int:cultivo_id>/', views.detalle_cultivo, name='detalle_cultivo'),
    path('suelos/', views.suelos, name='suelos'),
    path('galeria/', views.galeria, name='galeria'),
    path('productividad/', views.Productividad, name='productividad'),
]

path('suelos/<int:suelo_id>/', views.detalle_suelo, name='detalle_suelo'),

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cultivos/', views.cultivos, name='cultivos'),
    path('cultivos/<int:cultivo_id>/', views.detalle_cultivo, name='detalle_cultivo'),
    path('suelos/', views.suelos, name='suelos'),
    path('suelos/<int:suelo_id>/', views.detalle_suelo, name='detalle_suelo'),
    path('galeria/', views.galeria, name='galeria'),
    path('productividad/', views.Productividad, name='productividad'),
]