# gestion_biblioteca/models.py

from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    descripcion = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f'Prestamo de {self.libro.titulo} a {self.usuario}'