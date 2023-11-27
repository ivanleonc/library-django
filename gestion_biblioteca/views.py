# gestion_biblioteca/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro, Prestamo
from itertools import zip_longest
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required


def home(request):
    user_name = None
    if request.user.is_authenticated:
        user_name = f'{request.user.first_name} {request.user.last_name}'
    # Obtener los totales utilizando funciones de agregación de Django
    total_libros = Libro.objects.count()
    total_autores = Autor.objects.count()
    total_prestamos = Prestamo.objects.count()


    libros = Libro.objects.all()
    autores = Autor.objects.all() 
    prestamos = Prestamo.objects.all()

    # Agrupar los prestamos en conjuntos de tres
    prestamos_grouped = list(zip_longest(*[iter(prestamos)] * 3))
    # Agrupar los autores en conjuntos de tres
    autores_grouped = list(zip_longest(*[iter(autores)] * 3))
    # Agrupar los libros en conjuntos de tres
    libros_grouped = list(zip_longest(*[iter(libros)] * 3))

    context = {
        'total_libros': total_libros,
        'total_autores': total_autores,
        'total_prestamos': total_prestamos,
        'prestamos': prestamos_grouped,
        'libros': libros_grouped,
        'autores': autores_grouped,
        'user_name': user_name,
    }

    return render(request, 'home.html', context)

def autores(request):
    user_name = None
    if request.user.is_authenticated:
        user_name = f'{request.user.first_name} {request.user.last_name}'
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores, 'user_name': user_name} )

def libros(request):
    user_name = None
    if request.user.is_authenticated:
        user_name = f'{request.user.first_name} {request.user.last_name}'
    libros = Libro.objects.all()
    autores = Autor.objects.all() 
    return render(request, 'libros.html', {'libros': libros, 'autores': autores, 'user_name': user_name})

def prestamos(request):
    user_name = None
    if request.user.is_authenticated:
        user_name = f'{request.user.first_name} {request.user.last_name}'
    prestamos = Prestamo.objects.all()
    libros = Libro.objects.all()
    return render(request, 'prestamos.html', {'prestamos': prestamos, 'libros': libros, 'user_name': user_name})

def guardar_autor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        biografia = request.POST['biografia']
        autor = Autor(nombre=nombre, apellido=apellido, biografia=biografia)
        autor.save()
    return redirect('autores')

def editar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == 'POST':
        autor.nombre = request.POST['nombre']
        autor.apellido = request.POST['apellido']
        autor.biografia = request.POST['biografia']
        autor.save()
        return redirect('autores')

    return render(request, 'editar_autor.html', {'autor': autor})

def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect('autores')

def guardar_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        isbn = request.POST['isbn']
        descripcion = request.POST['descripcion']
        autor_id = request.POST['autor']
        autor = Autor.objects.get(id=autor_id)
        libro = Libro(titulo=titulo, isbn=isbn, descripcion=descripcion, autor=autor)
        libro.save()
    return redirect('libros')

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.isbn = request.POST['isbn']
        libro.descripcion = request.POST['descripcion']
        libro.autor = Autor.objects.get(id=request.POST['autor'])
        libro.save()
        return redirect('libros')

    autores = Autor.objects.all()
    return render(request, 'editar_libro.html', {'libro': libro, 'autores': autores})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect('libros')

def guardar_prestamo(request):
    if request.method == 'POST':
        libro_id = request.POST['libro']
        usuario = request.POST['usuario']
        fecha_prestamo = request.POST['fecha_prestamo']
        fecha_devolucion = request.POST['fecha_devolucion']
        libro = Libro.objects.get(id=libro_id)
        prestamo = Prestamo(libro=libro, usuario=usuario, fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion)
        prestamo.save()
    return redirect('prestamos')

def editar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)

    if request.method == 'POST':
        prestamo.libro = Libro.objects.get(id=request.POST['libro'])
        prestamo.usuario = request.POST['usuario']
        prestamo.fecha_prestamo = request.POST['fecha_prestamo']
        prestamo.fecha_devolucion = request.POST['fecha_devolucion']
        prestamo.save()
        return redirect('prestamos')

    libros = Libro.objects.all()
    return render(request, 'editar_prestamo.html', {'prestamo': prestamo, 'libros': libros})

def eliminar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    prestamo.delete()
    return redirect('prestamos')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión después del registro
            return redirect('login')  # Redirigir a la página principal
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Iniciar sesión
            return redirect('home')  # Redirigir a la página principal
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)  # Cerrar sesión
    return redirect('home')  # Redirigir a la página principal