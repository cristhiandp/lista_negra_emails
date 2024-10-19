# Lista Negra de Emails

Este es un proyecto desarrollado para la maestría en arquitectura de software. La aplicación permite la gestión de una lista negra de correos electrónicos, utilizando Flask y Postgres para el backend, con autenticación basada en JWT.

## Descripción del Proyecto

La aplicación ofrece dos endpoints principales:

- **Agregar correos a la lista negra**: Los usuarios pueden agregar correos electrónicos a una lista negra que se almacena en una base de datos Postgres.
- **Consultar la lista negra**: Los usuarios autenticados pueden consultar los correos electrónicos bloqueados.

### Tecnologías Utilizadas

- **Backend**: Flask con Flask-RESTful
- **Base de datos**: Postgres
- **Autenticación**: JWT (JSON Web Tokens)
- **Pruebas**: Unittest y Coverage para medir la cobertura del código.
- **Contenedores**: Docker y Docker Compose

---

## Estructura del Proyecto

```bash
lista_negra_emails/
├── postman              # Colección de postman
├── src/
│   ├── __init__.py
│   ├── db.py            # Configuración de la base de datos con SQLAlchemy
│   ├── decorators.py    # Decoradores personalizados para validación de JWT
│   ├── entities.py      # Definición de entidades SQLAlchemy
│   ├── main.py          # Punto de entrada de la aplicación Flask
│   ├── schemas.py       # Esquemas de Marshmallow para validación
│   └── services.py      # Lógica de negocio y endpoints RESTful
├── tests/               # Pruebas unitarias
│   ├── test_post.py     # Pruebas para los endpoints de la API
├── docker-compose.yml   # Configuración de Docker Compose
└── README.md            # Documentación del proyecto
```
---

## Configuración del Proyecto

### Variables de Entorno

El proyecto usa las siguientes variables de entorno para conectarse a la base de datos Postgres y configurar JWT:

- `FLASK_APP`: Ubicación del punto de entrada de la aplicación (`./src/main.py`).
- `DB_USER`: Usuario de la base de datos.
- `DB_PASSWORD`: Contraseña de la base de datos.
- `DB_NAME`: Nombre de la base de datos.
- `DB_HOST`: Host de la base de datos (en este caso, el servicio Postgres en Docker).
- `DB_PORT`: Puerto de la base de datos.
- `JWT_SECRET_KEY`: Clave secreta para la generación de tokens JWT.

### Docker Compose

El proyecto usa Docker Compose para orquestar los servicios. Para levantar el proyecto, asegúrate de tener Docker y Docker Compose instalados. Luego, ejecuta:

```bash
docker-compose up -d
```
Esto levantará los servicios dark_list y dark_list_db (Postgres), asegurándose de que estén correctamente conectados.

## Pruebas Unitarias y Cobertura de Código

El proyecto cuenta con pruebas unitarias para validar el funcionamiento de los endpoints y la lógica de negocio, utilizando el módulo `unittest`. Además, se utiliza `coverage.py` para asegurar una cobertura de código mínima del 70%.

### Ejecutar Pruebas y Validar Cobertura

Puedes ejecutar las pruebas unitarias y validar que la cobertura de código sea al menos del 70% usando el siguiente comando:

```bash
docker exec -it lista_negra_emails coverage run --source=src -m unittest discover -s tests && docker exec -it lista_negra_emails coverage report --fail-under=70
```
---

## Endpoints Disponibles

### Autenticación

- **POST `/login`**: Genera un token JWT para un usuario.

### Gestión de Lista Negra

- **GET `/blacklist`**: Consulta todos los correos electrónicos en la lista negra (requiere token).
- **POST `/blacklist`**: Agrega un correo electrónico a la lista negra (requiere token).

### Ejemplo de Colección de Postman

En la carpeta `postman`, se incluye una colección básica de Postman para interactuar con los endpoints de la API. Esta colección contiene ejemplos de cómo enviar solicitudes `GET` y `POST` con el token de autorización adecuado.

---

