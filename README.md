  # Crear las vistas para Clientes
app_mascotas/views.py (AGREGAR estas funciones):

     from django.shortcuts import render, redirect, get_object_or_404
    
    from .models import Animal, Cliente, Empleado

   # ==========================================
  # VISTAS PARA CLIENTES  
  # ==========================================

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
    
# 🔧 Paso 3: Actualizar el navbar
app_mascotas/templates/navbar.html (MODIFICAR la sección de Clientes):

    html
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom mb-4 rounded">
    <div class="container">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'inicio_mascotas' %}">
                        🏠 Inicio
                    </a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                        🐶 Mascotas
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="{% url 'agregar_mascota' %}">Agregar mascotas</a></li>
                        <li><a class="dropdown-item" href="{% url 'ver_mascotas' %}">Ver mascotas</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                        👥 Clientes
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="{% url 'inicio_clientes' %}">Inicio clientes</a></li>
                        <li><a class="dropdown-item" href="{% url 'agregar_cliente' %}">Agregar clientes</a></li>
                        <li><a class="dropdown-item" href="{% url 'ver_clientes' %}">Ver clientes</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                        👨‍💼 Empleados
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Agregar empleados</a></li>
                        <li><a class="dropdown-item" href="#">Ver empleados</a></li>
                        <li><a class="dropdown-item" href="#">Actualizar empleados</a></li>
                        <li><a class="dropdown-item" href="#">Borrar empleados</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
    </nav>
    
# 🔧 Paso 4: Agregar URLs para Clientes
app_mascotas/urls.py (MODIFICAR agregando las rutas de clientes):

    python
    from django.urls import path
    from . import views

    urlpatterns = [
    # URLs para Mascotas
    path('', views.inicio_mascotas, name='inicio_mascotas'),
    path('agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('ver/', views.ver_mascotas, name='ver_mascotas'),
    path('detalle/<int:id_animales>/', views.ver_detalle_mascota, name='detalle_mascota'),
    path('actualizar/<int:id_animales>/', views.actualizar_mascota, name='actualizar_mascota'),
    path('realizar-actualizacion/<int:id_animales>/', views.realizar_actualizacion_mascota, name='realizar_actualizacion_mascota'),
    path('borrar/<int:id_animales>/', views.borrar_mascota, name='borrar_mascota'),
    
    # NUEVAS URLs para Clientes
    path('clientes/', views.inicio_clientes, name='inicio_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar-actualizacion/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
    ]

# 🔧 Paso 5: Registrar modelos en admin
app_mascotas/admin.py (MODIFICAR):

    python
    from django.contrib import admin
    from .models import Animal, Cliente, Empleado

    @admin.register(Animal)
    class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id_animales', 'nombre', 'especie', 'edad', 'dueno']
    list_filter = ['especie', 'dueno']
    search_fields = ['nombre', 'especie']

    @admin.register(Cliente)
    class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 'nombre', 'apepaterno', 'correo', 'telefono']
    search_fields = ['nombre', 'apepaterno', 'correo']

    @admin.register(Empleado)
    class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id_empleado', 'nombre', 'apepaterno', 'ocupacion']
    search_fields = ['nombre', 'apepaterno', 'ocupacion']

# 🔧 Paso 6: Crear las plantillas para Clientes
app_mascotas/templates/clientes/inicio_clientes.html (CREAR):

    html
    {% extends 'base.html' %}

    {% block content %}
    <div class="row">
    <div class="col-md-8">
        <div class="card shadow-sm">
            <div class="card-body">
                <h2 class="card-title text-primary">👥 Gestión de Clientes</h2>
                <p class="card-text">
                    Sistema de administración para la gestión integral de clientes de la veterinaria. 
                    Aquí podrás realizar todas las operaciones CRUD necesarias para el correcto 
                    funcionamiento del establecimiento.
                </p>
                <h5 class="mt-4">Funcionalidades principales:</h5>
                <ul>
                    <li>Registro de nuevos clientes</li>
                    <li>Consulta de información de clientes</li>
                    <li>Actualización de datos personales</li>
                    <li>Eliminación de registros</li>
                    <li>Gestión de mascotas por cliente</li>
                </ul>
                <div class="mt-4">
                    <a href="{% url 'agregar_cliente' %}" class="btn btn-primary me-2">➕ Agregar Cliente</a>
                    <a href="{% url 'ver_clientes' %}" class="btn btn-success">📋 Ver Clientes</a>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card shadow-sm">
            <div class="card-body text-center">
                <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" 
                     alt="Clientes" class="img-fluid rounded">
                <h5 class="mt-3">Atención Personalizada</h5>
                <p class="text-muted">Para nuestros clientes</p>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}

# app_mascotas/templates/clientes/agregar_clientes.html (CREAR):

    html
    {% extends 'base.html' %}

    {% block content %}
    <div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card shadow-sm">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0">➕ Agregar Nuevo Cliente</h4>
            </div>
            <div class="card-body">
                <form method="POST">
                    {% csrf_token %}
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Nombre</label>
                            <input type="text" class="form-control" name="nombre" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Paterno</label>
                            <input type="text" class="form-control" name="apepaterno" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Materno</label>
                            <input type="text" class="form-control" name="apematerno" required>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Domicilio</label>
                        <input type="text" class="form-control" name="domicilio">
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Correo Electrónico</label>
                            <input type="email" class="form-control" name="correo" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Teléfono</label>
                            <input type="text" class="form-control" name="telefono" required>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Alergias</label>
                        <textarea class="form-control" name="alergias" rows="3" placeholder="Lista de alergias conocidas..."></textarea>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <button type="submit" class="btn btn-primary me-md-2">Guardar Cliente</button>
                        <a href="{% url 'ver_clientes' %}" class="btn btn-secondary">Cancelar</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}
  
  # app_mascotas/templates/clientes/ver_clientes.html (CREAR):

    html
    {% extends 'base.html' %}
  
    {% block content %}
    <div class="card shadow-sm">
    <div class="card-header bg-success text-white d-flex justify-content-between align-items-center">
        <h4 class="mb-0">📋 Lista de Clientes</h4>
        <a href="{% url 'agregar_cliente' %}" class="btn btn-light btn-sm">➕ Agregar Nuevo</a>
    </div>
    <div class="card-body">
        {% if clientes %}
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Apellidos</th>
                        <th>Correo</th>
                        <th>Teléfono</th>
                        <th>Domicilio</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {% for cliente in clientes %}
                    <tr>
                        <td>{{ cliente.id_cliente }}</td>
                        <td><strong>{{ cliente.nombre }}</strong></td>
                        <td>{{ cliente.apepaterno }} {{ cliente.apematerno }}</td>
                        <td>{{ cliente.correo }}</td>
                        <td>{{ cliente.telefono }}</td>
                        <td>{{ cliente.domicilio|default:"-" }}</td>
                        <td>
                            <a href="#" class="btn btn-info btn-sm">👁️ Ver</a>
                            <a href="{% url 'actualizar_cliente' cliente.id_cliente %}" class="btn btn-warning btn-sm">✏️ Editar</a>
                            <a href="{% url 'borrar_cliente' cliente.id_cliente %}" class="btn btn-danger btn-sm">🗑️ Borrar</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% else %}
        <div class="alert alert-info text-center">
            <h5>No hay clientes registrados</h5>
            <p>Comienza agregando el primer cliente al sistema.</p>
            <a href="{% url 'agregar_cliente' %}" class="btn btn-primary">Agregar Primer Cliente</a>
        </div>
        {% endif %}
    </div>
    </div>
    {% endblock %}
    
# app_mascotas/templates/clientes/actualizar_clientes.html (CREAR):

html

    {% extends 'base.html' %}

    {% block content %}
    <div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card shadow-sm">
            <div class="card-header bg-warning text-dark">
                <h4 class="mb-0">✏️ Actualizar Cliente: {{ cliente.nombre }}</h4>
            </div>
            <div class="card-body">
                <form method="POST" action="{% url 'realizar_actualizacion_cliente' cliente.id_cliente %}">
                    {% csrf_token %}
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Nombre</label>
                            <input type="text" class="form-control" name="nombre" value="{{ cliente.nombre }}" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Paterno</label>
                            <input type="text" class="form-control" name="apepaterno" value="{{ cliente.apepaterno }}" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Materno</label>
                            <input type="text" class="form-control" name="apematerno" value="{{ cliente.apematerno }}" required>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Domicilio</label>
                        <input type="text" class="form-control" name="domicilio" value="{{ cliente.domicilio }}">
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Correo Electrónico</label>
                            <input type="email" class="form-control" name="correo" value="{{ cliente.correo }}" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Teléfono</label>
                            <input type="text" class="form-control" name="telefono" value="{{ cliente.telefono }}" required>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Alergias</label>
                        <textarea class="form-control" name="alergias" rows="3">{{ cliente.alergias }}</textarea>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <button type="submit" class="btn btn-warning me-md-2">Actualizar Cliente</button>
                        <a href="{% url 'ver_clientes' %}" class="btn btn-secondary">Cancelar</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}

# app_mascotas/templates/clientes/borrar_clientes.html (CREAR):

html
      
      {% extends 'base.html' %}

    {% block content %}
    <div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card shadow-sm">
            <div class="card-header bg-danger text-white">
                <h4 class="mb-0">🗑️ Confirmar Eliminación</h4>
            </div>
            <div class="card-body text-center">
                <div class="alert alert-warning">
                    <h5>¿Estás seguro de que quieres eliminar este cliente?</h5>
                    <p class="mb-1"><strong>Nombre:</strong> {{ cliente.nombre }}</p>
                    <p class="mb-1"><strong>Apellidos:</strong> {{ cliente.apepaterno }} {{ cliente.apematerno }}</p>
                    <p class="mb-1"><strong>Correo:</strong> {{ cliente.correo }}</p>
                    <p class="mb-3"><strong>ID:</strong> {{ cliente.id_cliente }}</p>
                    <p class="text-danger"><strong>⚠️ Esta acción no se puede deshacer</strong></p>
                </div>
                
                <form method="POST">
                    {% csrf_token %}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                        <button type="submit" class="btn btn-danger me-md-2">Sí, Eliminar</button>
                        <a href="{% url 'ver_clientes' %}" class="btn btn-secondary">Cancelar</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}

# 🔧 Paso 7: Estructura final de carpetas
text
      
    UIII_mascotas_0237/
    ├── .venv/
    ├── backend_mascotas/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── app_mascotas/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── header.html
    │   │   ├── navbar.html
    │   │   ├── footer.html
    │   │   ├── inicio.html
    │   │   ├── mascotas/
    │   │   │   ├── agregar_mascotas.html
    │   │   │   ├── ver_mascotas.html
    │   │   │   ├── actualizar_mascotas.html
    │   │   │   ├── borrar_mascotas.html
    │   │   │   └── detalle_mascota.html
    │   │   └── clientes/                    # NUEVA CARPETA
    │   │       ├── inicio_clientes.html
    │   │       ├── agregar_clientes.html
    │   │       ├── ver_clientes.html
    │   │       ├── actualizar_clientes.html
    │   │       └── borrar_clientes.html
    ├── manage.py
    └── requirements.txt

# 🚀 Paso 8: Ejecutar migraciones y servidor
Terminal:

    bash
    # Crear migraciones para los cambios en admin
    python manage.py makemigrations

    # Aplicar migraciones
    python manage.py migrate

    # Ejecutar servidor en puerto 8037
    python manage.py runserver 8037

# ✅ Proyecto Completamente Funcional
Ahora tienes:

    ✅ CRUD completo para Clientes

    ✅ Diseño moderno con colores suaves

    ✅ Navegación actualizada en el navbar

    ✅ Estructura organizada de carpetas

    ✅ Modelos registrados en admin

    ✅ Sin uso de forms.py

# Accesos:

    http://127.0.0.1:8037/clientes/ - Inicio clientes

    http://127.0.0.1:8037/clientes/agregar/ - Agregar cliente

    http://127.0.0.1:8037/clientes/ver/ - Ver clientes

    http://127.0.0.1:8037/admin/ - Panel de administración

¡El CRUD de Clientes está listo y funcionando! 🎉
