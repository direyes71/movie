# Movie Api

Para ejecutar la API puede hacerse por medio del script Docker o por medio de ejecucion basado en virtualenv (Linux)

## Ejecucion con docker

```bash
docker-compose up
...
```
El comando anterior instalara las librerias necesarias para el proyecto y ejecutara la aplicacion en local en el puerto 8001

Para acceder a la documentacion de la API ir a la URL http://localhost:8001/doc/

## Ejecucion con virtualenv

Crear el entorno virtual con el gestor de entornos de python (recomendado virtualenvwrapper)

Instalar requirements

```bash
pip install -r requirements.txt
```

Ejecutar la aplicacion

```bash
python manage.py runserver
```

Para acceder a la documentacion de la API ir a la URL http://localhost:8000/doc/

Urls de la aplicacion

1.***Registro de usuarios***

```
/auth/sign-up/
```

Metodo ***POST*** 

Parametros

```
{
  "username": "string",
  "password": "string"
}
```

2.***Login de usuarios***

La autenticacion de usuarios esta basada en autenticacion con JWT

```
/auth/login-token/
```

Metodo ***POST*** 

Parametros

```
{
  "username": "string",
  "password": "string"
}
```

***Importante:*** Para la el envio del JWT Token en las peticiones debe enviarse el Header Authorization con la palabra "Bearer" seguido del JWTToken, como se muestra a continuacion 

```
{
    "Content-Type": "application/json",
    "Authorization": "Bearer {{JWTtoken}}"
}
```

3.***Logout***

```
/auth/logout/
```

Metodo ***POST*** 

4.***Registro de nueva pelicula***

```
/catalog/movie/
```

Metodo ***POST*** 

Parametros

```
{
  "name": "string",
  "duration": int,
  "year": int,
  "stars": int,
  "genre": "string",
  "director": "string"
}
```

5.***Consulta de una pelicula especifica***

```
/catalog/movie/{id}/
```

Metodo ***GET*** 

6.***Lista de peliculas***

```
/catalog/movie/
```

Metodo ***GET*** 

7.***Actualizacion de pelicula existente***

```
/catalog/movie/{id}/
```

Metodo ***PUT*** 

Parametros

```
{
  "name": "string",
  "duration": int,
  "year": int,
  "stars": int,
  "genre": "string",
  "director": "string"
}
```

8.***Eliminar pelicula existente***

```
/catalog/movie/{id}/
```

Metodo ***DELETE*** 

9.***Busqueda de peliculas***

```
/catalog/movie/?name=avengers&director=Russo&genre=accion
```

Metodo ***GET***

| QueryString | Descripción |
| ------------- | ------------- |
| name | Busca por el nombre de peliculas que contengan la palabra buscada |
| director | Busca peliculas por el nombre del director que contengan la palabra buscada |
| genre | Busca peliculas por el nombre del genero que contengan la palabra buscada |
| best_movie | Retorna las peliculas recomendadas, que contengan mas de 3 estrellas (Valor 1) |

10.***Listar las peliculas recomendadas***

```
/catalog/movie/?best_movie=1
```

Metodo ***GET***

| QueryString | Descripción |
| ------------- | ------------- |
| best_movie | Retorna las peliculas recomendadas, que contengan mas de 3 estrellas (Valor 1) |

***Puede usar la configuracion de Postman ubicada en la carpeta "postman" como ayuda para el consumo de los servicios Web.***

## Unitary Tests
Para ejecutar los test con coverage ejecutar los siguientes comandos

```bash
coverage run manage.py test
coverage report -m
```

El segundo comando mostrara el coverage del proyecto con relacion a las pruebas unitarias ***100%***
