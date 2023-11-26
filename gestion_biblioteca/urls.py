from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('autores/', views.autores, name='autores'),
    path('libros/', views.libros, name='libros'),
    path('prestamos/', views.prestamos, name='prestamos'),
    path('guardar_autor/', views.guardar_autor, name='guardar_autor'),
    path('guardar_libro/', views.guardar_libro, name='guardar_libro'),
    path('guardar_prestamo/', views.guardar_prestamo, name='guardar_prestamo'),
    path('editar_autor/<int:id>/', views.editar_autor, name='editar_autor'),
    path('eliminar_autor/<int:id>/', views.eliminar_autor, name='eliminar_autor'),
    path('editar_libro/<int:id>/', views.editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('editar_prestamo/<int:id>/', views.editar_prestamo, name='editar_prestamo'),
    path('eliminar_prestamo/<int:id>/', views.eliminar_prestamo, name='eliminar_prestamo'),
]
