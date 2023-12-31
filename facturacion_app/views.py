from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajador, Colegios, Cuotas, Facturas
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.shortcuts import render

def editar_colegio(request, rbd):
    # Obtén la instancia del colegio usando get_object_or_404 para manejar el caso en que no exista
    colegio = get_object_or_404(Colegios, rbd=rbd)

    if request.method == 'POST':
        # Obtener los datos del formulario POST
        rbd = int(request.POST['rbd'])
        rut_colegio = int(request.POST['rut'])
        nombre = request.POST['nombre']
        region = request.POST['region']
        comuna = request.POST['comuna']
        dependencia = request.POST['dependencia']
        fecha_ingreso = request.POST['fecha_ingreso']
        monto_plan = request.POST['monto_plan']

        # Actualizar los campos del colegio
        colegio.rbd = rbd
        colegio.rut_colegio = rut_colegio
        colegio.nombre = nombre
        colegio.region = region
        colegio.comuna = comuna
        colegio.dependencia = dependencia
        colegio.fecha_ingreso = fecha_ingreso
        colegio.monto_plan = monto_plan

        colegio.save()

        # Redirigir a la lista de colegios
        return redirect('lista_colegios')

    return render(request, 'editarColegio.html', {'colegio': colegio})


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
                # Agrega un mensaje de error genérico
                messages.error(request, 'Credenciales incorrectas')
        except Trabajador.DoesNotExist:
            # Agrega un mensaje de error genérico
            messages.error(request, 'Credenciales incorrectas')

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
            return redirect ('trabajador_login')        
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
        rut_trabajador = request.session.get('rut')
        if not rut_trabajador:
            # Si no hay rut en la sesión, redirige al login o muestra un error
            return redirect('trabajador_login')

        # Obtén la instancia del trabajador usando el rut
        try:
            trabajador_instance = Trabajador.objects.get(rut=rut_trabajador)
        except Trabajador.DoesNotExist:
            # Maneja el caso en que el trabajador no exista
            return redirect('trabajador_login')
        
        rbd = int(request.POST['rbd'])
        
        if Colegios.objects.filter(rbd=rbd).exists():
            messages.error(request, 'El RBD ya existe.')
        else:
            rut_colegio = int(request.POST['rut'])
            nombre = request.POST['nombre']
            region = request.POST['region']
            comuna = request.POST['comuna']
            dependencia = request.POST['dependencia']
            fecha_ingreso = request.POST['fecha_ingreso']
            monto_plan = request.POST['monto_plan']

            colegios = Colegios(
                trabajador=trabajador_instance,
                rbd = rbd,
                rut_colegio = rut_colegio,
                nombre = nombre,
                region = region,
                comuna = comuna,
                dependencia= dependencia,
                fecha_ingreso = fecha_ingreso,
                monto_plan =  monto_plan,
            )
            colegios.save()
            # Una vez que el colegio ha sido guardado, redirige al formulario de calendarización.
            # Aquí asumo que tienes una vista llamada 'agregar_calendarizacion' que se encarga de mostrar el segundo formulario.
            return redirect('agregar_calendarizacion', colegios_rbd=colegios.rbd)
    return render(request, 'agregarColegio.html')

def agregar_calendarizacion(request, colegios_rbd):
    colegios = Colegios.objects.get(rbd=colegios_rbd)
    return render(request, 'agregarCuotas.html', {'colegio': colegios})

def guardar_calendarizacion(request, colegio_rbd):
    try:
        print(request.POST)
        colegios = Colegios.objects.get(rbd=colegio_rbd)
        num_cuotas = request.POST['numero_cuotas']
        monto_total = colegios.monto_plan
        monto_cuota = monto_total / int(num_cuotas)

        for i in range(1, int(num_cuotas) + 1):
            fecha_cuota = request.POST['fecha_' + str(i)]
            Cuotas.objects.create(colegio=colegios, cuotas=num_cuotas, monto_cuota=monto_cuota, fecha_cuota=fecha_cuota)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        # Puedes hacer algo más aquí, como redirigir a una página de error o mostrar un mensaje.
        return redirect('error_page')
    else:
        return redirect('lista_colegios')
    
def get_cuotas(request, colegio_rbd):
    colegio = Colegios.objects.get(rbd=colegio_rbd)
    cuotas = Cuotas.objects.filter(colegio__rbd=colegio_rbd)
    
    cuotas_list = []
    for cuota in cuotas:
        cuota_dict = {
            "title": str(cuota.monto_cuota),
            "start": cuota.fecha_cuota.strftime('%Y-%m-%d'),
        }
        cuotas_list.append(cuota_dict)
    
    return JsonResponse(cuotas_list, safe=False)

def render_calendar(request, colegio_rbd):
    return render(request, 'calendario.html', {'colegio_rbd': colegio_rbd})

def listar_facturas(request, colegio_rbd):
    facturas = Facturas.objects.filter(colegio_id=colegio_rbd)
    return render(request, 'listarFacturas.html', {'facturas': facturas})

def agregar_factura(request, colegio_rbd):
    colegios = Colegios.objects.all()
    colegio_seleccionado = Colegios.objects.get(rbd=colegio_rbd)
    if request.method == 'POST':
        idfacturas = request.POST.get('idfacturas')
        total = request.POST.get('total')
        nota_credito = request.POST.get('nota_credito')
        estado_pago = request.POST.get('estado_pago')
        fecha_emision = request.POST.get('fecha_emision')
        colegio_instance = Colegios.objects.get(rbd=colegio_rbd)

        factura = Facturas(
            idfacturas = idfacturas,
            total=total,
            nota_credito=nota_credito,
            colegio=colegio_instance,
            fecha_emision=fecha_emision,
            estado_pago=estado_pago
        )
        factura.save()
        return redirect('listar_facturas', colegio_rbd=colegio_rbd)

    return render(request, 'agregarFactura.html', {'colegios': colegios, 'colegio_seleccionado': colegio_seleccionado})

def actualizar_factura(request, id_factura):
    # Obtén la instancia de Facturas usando get_object_or_404 para manejar el caso en que no exista
    factura = get_object_or_404(Facturas, pk=id_factura)
    if request.method == 'POST':
        nota_credito = request.POST.get('nota_credito')
        estado_pago = request.POST.get('estado_pago')
        fecha_pago = request.POST.get('fecha_pago')

        # Actualizar la factura
        factura.nota_credito = nota_credito
        factura.estado_pago = estado_pago
        factura.fecha_pago = fecha_pago
        factura.save()

        # Redirigir a la lista de facturas del colegio
        return redirect('listar_facturas', colegio_rbd=factura.colegio.rbd)
    
    # Si no es POST, simplemente redirige a la lista de facturas.
    return redirect('listar_facturas', colegio_rbd=factura.colegio.rbd)