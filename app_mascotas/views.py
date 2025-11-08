from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal, Cliente, Empleado

def inicio_mascotas(request):
    return render(request, 'inicio.html')

def agregar_mascota(request):
    if request.method == 'POST':
        # Crear nueva mascota con datos del formulario
        nueva_mascota = Animal(
            nombre=request.POST['nombre'],
            edad=request.POST['edad'],
            peso=request.POST['peso'],
            cuidados=request.POST['cuidados'],
            enfermedades=request.POST['enfermedades'],
            especie=request.POST['especie'],
            alimentacion=request.POST['alimentacion']
        )
        
        # Manejar la imagen si se proporciona
        if 'imagen' in request.FILES:
            nueva_mascota.imagen = request.FILES['imagen']
            
        nueva_mascota.save()
        return redirect('ver_mascotas')

    return render(request, 'mascotas/agregar_mascotas.html')

def ver_mascotas(request):
    mascotas = Animal.objects.all()
    return render(request, 'mascotas/ver_mascotas.html', {'mascotas': mascotas})

def ver_detalle_mascota(request, id_animales):
    mascota = get_object_or_404(Animal, id_animales=id_animales)
    return render(request, 'mascotas/detalle_mascota.html', {'mascota': mascota})

def actualizar_mascota(request, id_animales):
    mascota = get_object_or_404(Animal, id_animales=id_animales)
    return render(request, 'mascotas/actualizar_mascotas.html', {'mascota': mascota})

def realizar_actualizacion_mascota(request, id_animales):
    if request.method == 'POST':
        mascota = get_object_or_404(Animal, id_animales=id_animales)
        mascota.nombre = request.POST['nombre']
        mascota.edad = request.POST['edad']
        mascota.peso = request.POST['peso']
        mascota.cuidados = request.POST['cuidados']
        mascota.enfermedades = request.POST['enfermedades']
        mascota.especie = request.POST['especie']
        mascota.alimentacion = request.POST['alimentacion']
        
        # Manejar la imagen si se proporciona una nueva
        if 'imagen' in request.FILES:
            mascota.imagen = request.FILES['imagen']
            
        mascota.save()
        return redirect('ver_mascotas')

    return redirect('ver_mascotas')

def borrar_mascota(request, id_animales):
    mascota = get_object_or_404(Animal, id_animales=id_animales)

    if request.method == 'POST':
        mascota.delete()
        return redirect('ver_mascotas')

    return render(request, 'mascotas/borrar_mascotas.html', {'mascota': mascota})


def inicio_clientes(request):
    return render(request, 'clientes/inicio_clientes.html')

def agregar_cliente(request):
    if request.method == 'POST':
        # Crear nuevo cliente con datos del formulario
        nuevo_cliente = Cliente(
            nombre=request.POST['nombre'],
            apepaterno=request.POST['apepaterno'],
            apematerno=request.POST['apematerno'],
            domicilio=request.POST['domicilio'],
            correo=request.POST['correo'],
            telefono=request.POST['telefono'],
            alergias=request.POST['alergias']
        )
        nuevo_cliente.save()
        return redirect('ver_clientes')
    
    return render(request, 'clientes/agregar_clientes.html')

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id_cliente):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
        cliente.nombre = request.POST['nombre']
        cliente.apepaterno = request.POST['apepaterno']
        cliente.apematerno = request.POST['apematerno']
        cliente.domicilio = request.POST['domicilio']
        cliente.correo = request.POST['correo']
        cliente.telefono = request.POST['telefono']
        cliente.alergias = request.POST['alergias']
        cliente.save()
        return redirect('ver_clientes')
    
    return redirect('ver_clientes')

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})