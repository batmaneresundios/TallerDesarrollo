from django.contrib import admin
from django.urls import path
from facturacion_app import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('registro', views.trabajador_registro ,name="trabajador_registro"),
    path('login', views.trabajador_login ,name="trabajador_login"),
    path('lista_colegios/', views.listar_colegios, name="lista_colegios"),
    path('agregar_colegio/', views.agregar_colegio, name="agregar_colegio"),

]