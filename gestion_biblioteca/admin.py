from django.contrib import admin
from .models import Autor
from .models import Libro
from .models import Prestamo
# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Prestamo)
