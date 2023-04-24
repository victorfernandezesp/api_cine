"""
    En este programa se pretende: Mostrar géneros disponibles.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys


def muestra_generos_disponibles():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests

    URL_BASE = "https://api.themoviedb.org/3/"
    API_KEY = credenciales.API_KEY

    # Mandamos una petición al servidor y la almacenamos en Json
    url = f"{URL_BASE}genre/movie/list?api_key={API_KEY}"
    params = {"language": "es-ES"}
    try:
        respuesta_del_servidor = requests.get(url, params=params)
    except ConnectionError:
        print("No tienes conexión a internet, vuelve a intentarlo cuando tengas conexión. ")
        sys.exit(1)
    json_respuesta = respuesta_del_servidor.json()

    num_generos = len(json_respuesta["genres"])

    print(f"\n__________________________")
    print(f"Los géneros disponibles:\n")

    for i in range(num_generos):
        generos_disponibles = json_respuesta["genres"][i]["name"]
        print(f"   {i+1}.  {generos_disponibles}")
    print(f"________________________ \n\n")

if __name__ == '__main__':
    muestra_generos_disponibles()
