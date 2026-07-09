🎵 Registro Nacional de Fonogramas - Catálogo Digital
Esta aplicación web desarrollada en Django funciona como un catálogo colaborativo y sistema de reseñas tipo blog para melómanos y coleccionistas de música. Permite la digitalización, documentación y búsqueda de ediciones discográficas físicas en una base de datos centralizada.

Funcionalidades Principales
Panel de Administración Integral: Gestión centralizada de discos, usuarios y logs mediante la interfaz nativa de Django.

Sistema de Autenticación Completo: Registro seguro de nuevos usuarios, inicio de sesión y cierre de sesión con redirecciones automatizadas.

Catálogo Colaborativo: Los usuarios registrados pueden dar de alta nuevos fonogramas y editar la información existente.

Buscador en Tiempo Real: Barra de búsqueda inteligente en la portada que filtra por artista o título del álbum.

Reseñas Estructuradas: Formato tipo blog integrado en la ficha técnica de cada disco para comentarios y análisis musical.

Instrucciones para Ejecución Local
Seguí estos pasos para clonar y ejecutar el proyecto en tu entorno local:

Requisitos Previos
Python 3.10 o superior instalado.

1. Clonar el repositorio
git clone https://github.com/alemorenolegaspi-prog/ProyectoPYcoderhouse.git
cd ProyectoPYcoderhouse

2. Configurar el Entorno Virtual
python -m venv env
.\env\Scripts\Activate.ps1

3. Instalar Dependencias
pip install -r requirements.txt

4. Ejecutar Migraciones y Servidor
python manage.py migrate
python manage.py runserver

El sitio estará disponible en: http://127.0.0.1:8000/

Despliegue en Producción
El proyecto cuenta con la configuración de archivos estáticos lista para producción y recolectada mediante collectstatic. Aplicación preparada para simulación de despliegue mediante estructura modular.
