from django.shortcuts import render, redirect
from .models import Elemento, Albergue, Hospital, Bombero, CruceArroyo, Incidente
from .models import Albergue, Hospital
from django.urls import reverse

def index(request):
    # Obtén los albergues y hospitales desde la base de datos
    albergues = Albergue.objects.all()
    hospitales = Hospital.objects.all()
    bomberos = Bombero.objects.all()
    # Pasa los datos a la plantilla
    context = {
        'albergues': albergues,
        'hospitales': hospitales,
        'bombero': bomberos,
    }

    # Renderiza la plantilla con los datos
    return render(request, 'inicio/index.html', context)

def registrar_elemento(request):
    elemento_coordenadas = None

    if request.method == 'POST':
        tipo_elemento = request.POST.get('tipoElemento')
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')

        elemento = Elemento.objects.create(
            tipo=tipo_elemento,
            latitud=latitud,
            longitud=longitud,
        )

        if tipo_elemento == 'Albergue':
            ocupacion_actual = request.POST.get('ocupacion_actual')
            ocupacion_total = request.POST.get('ocupacion_total')
            estado_albergue = request.POST.get('estadoAlbergue')  # Cambiado a 'estado_albergue'
            suministro_albergue = request.POST.get('suministroAlbergue')  # Cambiado a 'suministro_albergue'
            telefonos_albergue = request.POST.get('telefonoAlbergue')  # Cambiado a 'telefonos_albergue'

            albergue = Albergue.objects.create(
                elemento=elemento,
                ocupacion_actual=ocupacion_actual,
                ocupacion_total=ocupacion_total,
                estado=estado_albergue,  # Cambiado a 'estado_albergue'
                suministro_electrico=suministro_albergue,  # Cambiado a 'suministro_albergue'
                telefonos=telefonos_albergue  # Cambiado a 'telefonos_albergue'
            )

            # Obtener las coordenadas del elemento asociado al Albergue
            elemento_coordenadas = {
                'latitud': albergue.elemento.latitud,
                'longitud': albergue.elemento.longitud,
                'descripcion': f'<strong>Albergue</strong><p>Ocupación actual: {ocupacion_actual}</p>'
            }

        elif tipo_elemento == 'Hospital':
            disponibilidad = request.POST.get('disponibilidad')
            estado_hospital = request.POST.get('estadoHospital')
            telefonos_hospital = request.POST.get('telefonoHospital')

            hospital = Hospital.objects.create(
                elemento=elemento,
                disponibilidad=disponibilidad,
                estado=estado_hospital,
                telefonos=telefonos_hospital
            )

            # Obtener las coordenadas del elemento asociado al Hospital
            elemento_coordenadas = {
                'latitud': hospital.elemento.latitud,
                'longitud': hospital.elemento.longitud,
                'descripcion': f'<strong>Hospital</strong><p>Disponibilidad: {disponibilidad}</p>'
            }

        elif tipo_elemento == 'Bombero':
            suministro_bombero = request.POST.get('suministroBombero')
            telefonos_bombero = request.POST.get('telefonos_bombero')

            bombero = Bombero.objects.create(
                elemento=elemento,
                suministro_electrico=suministro_bombero,
                telefonos=telefonos_bombero
            )

            # Obtener las coordenadas del elemento asociado al Bombero
            elemento_coordenadas = {
                'latitud': bombero.elemento.latitud,
                'longitud': bombero.elemento.longitud,
                'descripcion': f'<strong>Bombero</strong><p>Suministro eléctrico: {suministro_bombero}</p>'
            }

        elif tipo_elemento == 'CruceArroyo':
            condicion = request.POST.get('condicion')
            detalles_arroyo = request.POST.get('detalles_arroyo')

            cruceArroyo = CruceArroyo.objects.create(
                elemento=elemento,
                condicion=condicion,
                detalles=detalles_arroyo
            )

            # Obtener las coordenadas del elemento asociado al Cruce de arroyo
            elemento_coordenadas = {
                'latitud': cruceArroyo.elemento.latitud,
                'longitud': cruceArroyo.elemento.longitud,
                'descripcion': f'<strong>Cruce de arroyo</strong><p>Detalles: {detalles_arroyo}</p>'
            }

        elif tipo_elemento == 'Incidente':
            detalles_incidente = request.POST.get('detalles_incidente')

            incidente = Incidente.objects.create(
                elemento=elemento,
                detalles=detalles_incidente
            )

            # Obtener las coordenadas del elemento asociado al Incidente
            elemento_coordenadas = {
                'latitud': incidente.elemento.latitud,
                'longitud': incidente.elemento.longitud,
                'descripcion': f'<strong>Incidente en vía pública</strong><p>Detalles: {detalles_incidente}</p>'
            }
        return redirect(reverse('inicio:home'))
    return render(request, 'inicio/elemento.html', {'elemento_coordenadas': elemento_coordenadas})

def editar_elemento(request):
    albergues = Albergue.objects.all()
    return render(request, 'inicio/editar.html')
