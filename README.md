# API-MercaTodo

_Este proyecto coloca en práctica, las habilidades de trabajo colaborativo utilizando el control de versiones git, github, herokus (plataforma de servicios en la nube) y los conocimientos adquiridos sobre Python, Django, MySQL. En el bootcamp prográmate de la fundación Educamás._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

1- Abre la Git Bash.

2- Cambia el directorio de trabajo actual a la ubicación en donde quieres clonar el directorio.

3- Escribe git clone, y luego pega la URL que copiaste antes.

- $ git clone https://github.com/SebasO8/API-MercaTodo.git

4- Presiona Enter para crear tu clon local.

Mira **Deployment** para conocer como desplegar el proyecto.

### Instalación 🔧

_**Nota:** los comandos se ejecutaron el intérprete de comando de Windows, (en inglés, 'Command Prompt', también conocido como **cmd.exe** o simplemente **cmd**), después de la creación de la carpeta se inicializo el repositorio de git y github, se configuro el archivo gititnore._

1- Crear la carpeta para instalar el entorno virtual:

- Projects> mkdir Mercatodo_API
- Projects> cd Mercatodo_API

2- Instalamos el entorno virtual:

- Mercatodo_API> python -m venv venv

3- Activar el entorno virtual:

- Mercatodo_API> cd venv\Scripts\activate
- Comando para activar el venv: activate
- Comando para desactivar el venv: deactivate

4- Instalar Django en el entorno virtual:

- Scripts> pip install django

5- Verificamos si django está instalado:

- Scripts> python -m django –-version

6- Crea un nuevo proyecto en django:

- Scripts> cd ../../
- Mercatodo_API> django-admin startproject Project_API

7- Crea una nueva aplicación en django:

- Mercatodo_API> cd Project_API
- Project_API> python manage.py startapp api

8- Inicializar el servidor de desarrollo:

- Project_API> python manage.py runserver

9- Configurar MySQL con Django:

- Project_API> pip install mysqlclient
- **Nota:** Se debe crear la db (mercatodo) en el gestor de base de datos de mysql

10- Ejecutar las migraciones para que se aplique en la base de datos:

- Project_API> python manage.py migrate

11- Creación del súper usuario:

- Project_API> python manage.py createsuperuser
- Nombre de usuario (leave blank to use 'xxxxxxx'): admin
- Dirección de correo electrónico: xxxxxxa@hotmail.com
- Password:
- Password (again):
- Superuser created successfully.

12- Inicializar el servidor de desarrollo:

- Project_API> python manage.py runserver

13- Aplicamos la migración de los modelos _(Crea el archivo de migración )_:

- Project_API> python manage.py makemigrations

14- Ejecutar las migraciones para que se aplique en la base de datos:

- Project_API> python manage.py migrate:

15- creación de un archivo requirements.txt

- Project_API> pip freeze > requirements\requirements.txt

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Las herramientas utilizadas para este proyecto fueron:_

- [python](https://www.python.org/) - Usado como
  Lenguaje de programación
- [django](https://www.djangoproject.com/) - El framework web usado
- [pip](https://pypi.org/project/Django/) - Sistema de gestión de paquetes
- [MySQ](https://www.mysql.com/) - Sistema de gestión de bases de datos relacional
- [MySQL Workbench](https://www.mysql.com/products/workbench/) - Herramienta visual de diseño de bases de datos

## Autores ✒️

- **Yanith rodríguez** - [yicell52](https://github.com/yicell52)
- **Nicolás Sánchez** - [NiicolasDev](https://github.com/NiicolasDev)
- **Sebastián Ocampo** - [SebasO8](https://github.com/SebasO8)
- **Guillermo Garcia Soto** - [Gasogui](https://github.com/Gasogui)

## Expresiones de Gratitud 🎁

- Fundación educamás – Prográmate (bootcamp).
- Formadores y Co formadores - Prográmate (bootcamp).
- Simplon.co Grand Ouest.
- A todos los compañeros del bootcamp.
