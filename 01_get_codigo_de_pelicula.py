"""
    Apartado 1:
        Buscar código de película según su nombre.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

# Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
import credenciales
import requests
API_KEY = credenciales.API_KEY

# Preguntamos al usuario la pelicula
pelicula = input("¿De qué película quieres saber su código?:    ")

# Mandamos una petición al servidor y la almacenamos en Json
respuesta_del_servidor = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=es-ES&query={pelicula}")
json_respuesta = respuesta_del_servidor.json()

# Almacenamos en variables los resultados obtenidos, que queramos, del Json
titulo = json_respuesta["results"][0]["title"]
id_pelicula = json_respuesta["results"][0]["id"]
ano_de_lanzamiento = json_respuesta["results"][0]["release_date"]

# Mostramos los resultados
print(f"El id de la película: {titulo}({ano_de_lanzamiento[0:4]}) es: {id_pelicula}")

