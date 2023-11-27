# library-django

# Configuración del Entorno para el Proyecto Biblioteca

## Crear un entorno virtual

```bash
py -m venv env
source env/Scripts/activate
pip install django
cd biblioteca/
python manage.py runserver

Ahora puedes acceder a la aplicación en tu navegador usando las siguientes URLs:

http://127.0.0.1:8000/ - Vista principal de la aplicación.
http://127.0.0.1:8000/admin - Panel de administración.
Credenciales para el panel de administración:

Usuario: ivanleonc
Contraseña: admin