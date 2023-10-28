from django.shortcuts import render, redirect
from .models import Trabajador, Colegios
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password

from django.shortcuts import render

def trabajador_login(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        password = request.POST.get('password')

        try:
            trabajador = Trabajador.objects.get(rut=rut)
            
            # Comprobamos si la contraseña es correcta
            if check_password(password, trabajador.password):
                # Aquí puedes manejar la creación de sesiones o tokens si lo deseas
                request.session['rut'] = trabajador.rut
                return redirect('lista_colegios')  # Redirige al template listaColegios
            else:
                # Aquí puedes agregar un mensaje de error si la contraseña es incorrecta
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})

        except Trabajador.DoesNotExist:
            # Aquí puedes agregar un mensaje de error si el RUT no existe
            return render(request, 'login.html', {'error': 'RUT no registrado'})
    return render(request, 'login.html')  # Esta es la página de inicio de sesión

def trabajador_registro(request):
    if request.method == 'POST':
        try:
            rut = request.POST.get('rut')
            password = make_password(request.POST.get('password'))  # Ciframos la contraseña antes de guardarla
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            correo = request.POST.get('correo')

            trabajador = Trabajador(rut=rut, password=password, nombre=nombre, apellido=apellido, correo=correo)
            trabajador.save()
        
            return JsonResponse({'status': 'registered'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        # Si es una petición GET, simplemente retornamos el formulario de registro
        return render(request, 'trabajadorRegistro.html')
    
def listar_colegios(request):
    if 'rut' in request.session:
        rut = request.session['rut']
        colegios = Colegios.objects.filter(trabajador__rut=rut).select_related('trabajador')
        return render(request, 'listaColegios.html', {'colegios': colegios})
    else:
        return redirect('trabajador_login')

  
def agregar_colegio(request):
    if request.method == 'POST':
        rbd = int(request.POST['rbd'])
        rut_colegio = int(request.POST['rut'])
        nombre = request.POST['nombre']
        region = request.POST['region']
        comuna = request.POST['comuna']
        dependencia = request.POST['dependencia']
        fecha_ingreso = request.POST['fecha_ingreso']
        monto_plan = request.POST['monto_plan']
        mes_facturacion = request.POST['mes_facturacion']

        colegios = Colegios(
            rbd = rbd,
            rut_colegio = rut_colegio,
            nombre = nombre,
            region = region,
            comuna = comuna,
            dependencia= dependencia,
            fecha_ingreso = fecha_ingreso,
            monto_plan =  monto_plan,
            mes_facturacion = mes_facturacion
            )
        colegios.save()

        return redirect('Listacolegios')
    return render(request, 'AgregarColegio.html')

