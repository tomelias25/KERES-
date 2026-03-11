from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cultivos/', views.cultivos, name='cultivos'),
    path('suelos/', views.suelos, name='suelos'),
    path('galeria/', views.galeria, name='galeria'),
    path('dashboard/', views.dashboard, name='dashboard'),
]