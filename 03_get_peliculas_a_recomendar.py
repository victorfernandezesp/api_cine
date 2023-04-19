"""
    Apartado 3:
        Películas a recomendar si nos gusta una película concreta.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

# Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
import credenciales
import requests
API_KEY = credenciales.API_KEY

# Preguntamos al usuario la pelicula
pelicula = input("Dime que pelicula te gusta y te recomendare varias más:    ")

# Mandamos una petición al servidor y la almacenamos en Json
respuesta_del_servidor_id_pelicula = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=es-ES&query={pelicula}")
json_respuesta_id_pelicula = respuesta_del_servidor_id_pelicula.json()
id_pelicula = json_respuesta_id_pelicula["results"][0]["id"]

respuesta_del_servidor = requests.get(f"https://api.themoviedb.org/3/movie/{id_pelicula}/recommendations?api_key={API_KEY}&language=es-ES")
json_respuesta = respuesta_del_servidor.json()

num_peliculas = int(input("¿Cuántas películas quieres que te recomiende?:   "))
print("-------------------------------------------------------------------------------------------------------------\n")
print(f"Películas que te recomendadas a partir de {pelicula}:\n")
for i in range(num_peliculas):
    pelicula_recomendada = json_respuesta["results"][i]["title"]
    print(f"{i+1}.  {pelicula_recomendada}")
    argumento = json_respuesta["results"][i]["overview"]
    print(f"    Trama argumental: \n {argumento} \n")

print("\n-------------------------------------------------------------------------------------------------------------")
