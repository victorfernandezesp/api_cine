"""
    Apartado 5:
        Mostrar géneros disponibles.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

# Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
import credenciales
import requests
API_KEY = credenciales.API_KEY

# Mandamos una petición al servidor y la almacenamos en Json
respuesta_del_servidor = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=es-Es")
json_respuesta = respuesta_del_servidor.json()

num_generos = len(json_respuesta["genres"])
print("-------------------------------------------------------------------------------------------------------------\n")
print(f"Los géneros disponibles:")
for i in range(num_generos):
    generos_disponibles = json_respuesta["genres"][i]["name"]
    print(f"{i+1}.  {generos_disponibles}")

print("\n-------------------------------------------------------------------------------------------------------------")
