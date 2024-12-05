from django.shortcuts import render,get_object_or_404,redirect
#---->Importamos el Sector de Formularios
from .forms import *
from .models import *
from django.contrib import messages  
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def Home(request):
    buscar=Vehiculos.objects.all().order_by('-Codigo')[:6]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)



def Agregar(request):
    data={
        'forms':NuevoVehiculos()
    }
    if request.method=='POST':
        query=NuevoVehiculos(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Registrados"
        else:
            data['forms']=NuevoVehiculos
    return render (request,'Pages/agregar.html',data)

def ver_Vehiculos(request):
    #--->TREAMOS TODOS LOS ELEMENTOS DEL TABLA
    buscar=Vehiculos.objects.all()
    data={
        'forms':buscar
    }
    return render(request,'Pages/visualizar.html',data)


def Modificar_Vehiculos(request,Codigo):
    sql=get_object_or_404(Vehiculos,Codigo=Codigo)
    data={
        'forms':NuevoVehiculos(instance=sql)
    }
    if request.method=='POST':
        query=NuevoVehiculos(data=request.POST,instance=sql,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Modificados Correctamente "
        else:
            data['forms']=NuevoVehiculos
    return render (request,'Pages/modificar.html',data)

# boton eliminar

def Eliminar_Vehiculos(request,Codigo):
    buscar=get_object_or_404(Vehiculos,Codigo=Codigo)
    buscar.delete()
    return redirect(to="visualizar")


def detalle_vehiculo(request, Codigo):
    vehiculo = get_object_or_404(Vehiculos, Codigo=Codigo)
    alerta_stock = None  # Inicializar mensaje como None

      # Verifica si la cantidad es 2 o menos y genera un mensaje
    if vehiculo.Cantidad <= 2:
        alerta_stock = "Quedan pocas unidades disponibles de este vehículo."
    else:
        alerta_stock = ""  # Si no hay alerta, envía una cadena vacía
    return render(request, 'pages/detalle_vehiculo.html', {'vehiculo': vehiculo, 'alerta_stock': alerta_stock})

#Carritoo
def agregar_al_carrito(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculos, Codigo=vehiculo_id)  # Usamos el modelo Vehiculos
    carrito = request.session.get('carrito', {})

    # Si el vehículo ya está en el carrito, aumentamos la cantidad
    if str(vehiculo.Codigo) in carrito:
        carrito[str(vehiculo.Codigo)]['cantidad'] += 1
    else:
        carrito[str(vehiculo.Codigo)] = {
            'modelo': vehiculo.Modelo,
            'marca': vehiculo.Marca,
            'precio': str(vehiculo.Precio),
            'cantidad': 1
        }

    request.session['carrito'] = carrito  # Guardamos el carrito actualizado en la sesión
    return redirect('ver_carrito')  # Redirigimos a la página del carrito


def agregar_al_carrito(request, vehiculo_id):
    # Recuperar el carrito de la sesión, o inicializar uno vacío
    carrito = request.session.get('carrito', {})
    
    # Obtener el vehículo por su ID
    vehiculo = get_object_or_404(Vehiculos, Codigo=vehiculo_id)

    # Si ya está en el carrito, aumentar la cantidad
    if str(vehiculo.Codigo) in carrito:
        carrito[str(vehiculo.Codigo)]['cantidad'] += 1
    else:
        # Si no está, agregarlo al carrito
        carrito[str(vehiculo.Codigo)] = {
            'modelo': vehiculo.Modelo,
            'marca': vehiculo.Marca,
            'precio': vehiculo.Precio,
            'cantidad': 1,
        }
    
    # Guardar el carrito actualizado en la sesión
    request.session['carrito'] = carrito
    return redirect('visualizar')  # Redirigir a la página de visualización

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    carrito_detalles = []

    for vehiculo_id, vehiculo in carrito.items():
        vehiculo['id'] = vehiculo_id  # Asegúrate de agregar el ID al diccionario
        vehiculo['subtotal'] = float(vehiculo['precio']) * vehiculo['cantidad']
        carrito_detalles.append(vehiculo)

    total = sum(item['subtotal'] for item in carrito_detalles)

    return render(request, 'Pages/ver_carrito.html', {'carrito': carrito_detalles, 'total': total})





def eliminar_del_carrito(request, vehiculo_id):
    carrito = request.session.get('carrito', {})

    # Si el vehículo está en el carrito, lo eliminamos
    if str(vehiculo_id) in carrito:
        del carrito[str(vehiculo_id)]

    request.session['carrito'] = carrito  # Actualizamos el carrito en la sesión
    return redirect('ver_carrito')  # Redirigimos a la página del carrito



def actualizar_carrito(request, vehiculo_id, cantidad):
    carrito = request.session.get('carrito', {})

    # Si el vehículo está en el carrito y la cantidad es válida
    if str(vehiculo_id) in carrito:
        if cantidad > 0:
            carrito[str(vehiculo_id)]['cantidad'] = cantidad  # Actualizamos la cantidad
        else:
            del carrito[str(vehiculo_id)]  # Si la cantidad es 0 o menor, lo eliminamos

    request.session['carrito'] = carrito  # Guardamos el carrito actualizado en la sesión
    return redirect('ver_carrito')  # Redirigimos a la página del carrito
