from django.contrib import admin
from django.urls import path
from facturacion_app import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('registro', views.trabajador_registro ,name="trabajador_registro"),
    path('', views.trabajador_login ,name="trabajador_login"),
    path('lista_colegios/', views.listar_colegios, name="lista_colegios"),
    path('agregar_colegio/', views.agregar_colegio, name="agregar_colegio"),
    path('agregar_cuotas/<int:colegios_rbd>/', views.agregar_calendarizacion, name="agregar_calendarizacion"),
    path('guardar_cuotas/<int:colegio_rbd>/', views.guardar_calendarizacion, name="guardar_calendarizacion"),
    path('get_cuotas/<int:colegio_rbd>/', views.get_cuotas, name='get_cuotas'),
]