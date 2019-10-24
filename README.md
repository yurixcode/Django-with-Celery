# Prueba Django Celery - 1 docker multiworker

## Descripción del proyecto

Proyecto de prueba para lanzar una tarea larga con Django de forma asíncrona utilizando el sistema de cola de tareas Celery y el broker de mensajería RabbitMQ/Redis.
Arquitectura para lanzar múltiples workers de Celery en un mismo Docker.

## Dependencias / Requisitos (requirements)

### Python

Dado que el desarrollo del backend se apoya en Django, es necesario tener instalado en el sistema una versión de Python,
en nuestro caso, de 64 bits. Al menos la versión 3.7, que es la actual en el momento de la redacción de este documento,
aunque otras versiones 3.x pueden ser perfectamente compatibles. Para descargar Python: https://www.python.org/downloads/

### Docker

Para dar soporte a los contenedores y que la configuración del entorno hace uso de docker-compose. Para descargar docker
para Windows: https://store.docker.com/editions/community/docker-ce-desktop-windows.

## Instrucciones de instalación

La instalación consta de la preparación del entorno en docker junto con la instalación de dependencias.

```
$ virtualenv env
$ env\Scripts\activate
$ pip install -r requirements
```

```
$ docker-compose build
$ docker-compose up
```


## Cómo colaborar en este proyecto

```
$ git clone https://tecnoNP.GitLab.movisat.com/eescriba/prueba-django-celery.git
$ virtualenv env
$ env\Scripts\activate
$ pip install -r requirements
```

## Cómo realizar pruebas

TODO


## Tecnologías

- Python: https://www.python.org/
- Django: https://www.djangoproject.com/
- Django Rest Framework: https://www.django-rest-framework.org/
- Docker: https://www.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- PostgreSQL: https://www.postgresql.org/
- Celery: http://www.celeryproject.org/
- RabbitMQ: https://www.rabbitmq.com/
- Redis: https://redis.io/

