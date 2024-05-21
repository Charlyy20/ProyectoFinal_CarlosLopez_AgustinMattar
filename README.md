# Proyecto Final CoderHosue
Comision: 54135
Alumnos: Lopez Carlos David y Agustin Elias Mattar Insua

# Acerca del proyecto
Este proyecto es un E.commerce, dedicado al mundo automotor con prductos aftermarket.

# Aplicaciones
- Core
- Products
- Register

# Modelos
- Persona
- Contacto
- Cuenta
- Products
- Llanta
- Aleron
- Intake
- Spoiler
- Widebody

# Mejoras Futuras
- Mejorar el Responsive
- Redirecciones del Footer funcionando
- Carrito de Compras
- Perfiles de Usuarios

# Problemas Conocidos
- Hubo problemas con el Branch "Mattar-Dev". Por alguna razon desconocida el codigo dejo de correr y tirar errores en el .venv. 
  El branch se dejo para poder constatar los commit realizados antes del problema.

# Aclaraciones
- Lo que es la imagen se aplico a los productos, para que de esa manera se pueda cargar una imagen. Asi tambien para mostrarla en la card y luego en el portfolio-details

# Lista de Comandos Utiles

`mkdir nueva_carpeta`
> Crea una carpeta llamada nueva_carpeta

`ls`
> Muestra la lista de archivos

`cd nueva_carpeta`
> Cambia de carpeta

`pwd`
> Muestra la ruta actual

`python -m venv .venv`
> Crea un entorno virtual llamado .venv

`source .venv/bin/activate`
> Activa el entorno virtual en Linux o Mac

`.\venv\Scripts\activate`
> Activa el entorno virtual en Windows

`pip list`
> Muestra la lista de paquetes disponibles en el entorno virtual

`pip install django`
> Instala Django

`pip freeze >> requirements.txt`
`pip install -r requirements.txt`
> Crea un archivo de requisitos con todo lo instalado

`django-admin startproject config .`
> Crea un proyecto en el directorio actual

`python manage.py runserver`
> Ejecuta el servidor

`python manage.py startapp app`
> Crea una nueva aplicación llamada app

`python manage.py makemigrations`
> Crea las migraciones, que son archivos Python encargados de la base de datos

`python manage.py migrate`
> Ejecuta las migraciones, para que se realicen los cambios en la base de datos

`python manage.py createsuperuser`
> Crea un usuario administrador para acceder a 127.0.0.1:8000/admin