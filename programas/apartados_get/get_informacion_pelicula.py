"""
    En este programa se pretende: Mostrar información de película según su código.
    Información a mostrar:
        *   Título.
        *   Géneros.
        *   Argumento.
        *   Duración.
        *   Enlace a su web en IMDB.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys


def muestra_info_de_pelicula():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests

    URL_BASE = "https://api.themoviedb.org/3/"
    API_KEY = credenciales.API_KEY
    while True:
        codigo_de_pelicula = input("Dame el código de la película a buscar y te daré información de ella:    ")
        # Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
        url = f"{URL_BASE}movie/{codigo_de_pelicula}?api_key={API_KEY}"
        params = {"language": "es-ES"}
        try:
            respuesta_del_servidor = requests.get(url, params=params)
        except ConnectionError:
            print("No tienes conexión a internet, vuelve a intentarlo cuando tengas conexión. ")
            sys.exit(1)
        json_respuesta = respuesta_del_servidor.json()

        """Se guarda la información que se desea en variables y se muestran
         No podemos comprobar mediante el json el número de películas existentes para saber si hay o no resultados,
         así que hacemos un try que desempeña la misma función."""
        try:
            json_respuesta["title"]
        except KeyError:
            print("No existe una película con dicho código")
            continue
        break

    titulo = json_respuesta["title"]
    num_generos = len(json_respuesta["genres"])
    lista_de_generos = []
    for i in range(num_generos):
        genero = json_respuesta["genres"][i]["name"]
        lista_de_generos.append(genero)
    argumento = json_respuesta["overview"]
    duracion = json_respuesta["runtime"]
    horas = int(duracion) // 60
    minutos = int(duracion) % 60
    id_imdb = json_respuesta["imdb_id"]

    print("-------------------------------------------------------------------------------------------------------------\n")
    print(f"ID de la película: {codigo_de_pelicula}")
    print(f"Título: {titulo}")
    print("Géneros:", ", ".join(lista_de_generos))
    print(f"Duración: {horas} horas {minutos} minutos")
    print(f"Enlace a IMDb: https://www.imdb.com/title/{id_imdb}")
    print(f"Argumento: {argumento}")
    print("\n-------------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    muestra_info_de_pelicula()
