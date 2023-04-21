"""
    En este programa se pretende: Encontrar películas a recomendar introduciendo una película de referencia.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys


def muestra_recomendaciones_de_peliculas():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests

    URL_BASE = "https://api.themoviedb.org/3/"
    API_KEY = credenciales.API_KEY

    pelicula = input("Dime que película te gusta y te recomendaré varias más:    ")
    # Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
    url = f"{URL_BASE}search/movie?api_key={API_KEY}"
    params = {"query": {pelicula}, "language": "es-ES"}
    respuesta_del_servidor_id_pelicula = requests.get(url, params=params)
    json_respuesta_id_pelicula = respuesta_del_servidor_id_pelicula.json()

    comprueba_que_existe_pelicula(json_respuesta_id_pelicula)

    id_pelicula = json_respuesta_id_pelicula["results"][0]["id"]
    contador_paginas = 1

    # Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
    url = f"{URL_BASE}movie/{id_pelicula}/recommendations?api_key={API_KEY}"
    # Se saca la información de las películas, se almacena y se muestra
    while True:
        params = {"language": "es-ES", "page": {contador_paginas}}
        respuesta_del_servidor = requests.get(url, params=params)
        json_respuesta = respuesta_del_servidor.json()

        num_paginas = json_respuesta["total_pages"]
        numero_de_pelis_por_pagina = len(json_respuesta["results"])


        print("-------------------------------------------------------------------------------------------------------------\n")
        print(f"Películas que te recomendadas a partir de {pelicula}:\n")
        for i in range(numero_de_pelis_por_pagina):
            pelicula_recomendada = json_respuesta["results"][i]["title"]
            argumento = json_respuesta["results"][i]["overview"]
            print("_______\n")
            print(f"Título: {pelicula_recomendada}")
            print(f"Trama argumental:   {argumento} \n")
        print("\n-------------------------------------------------------------------------------------------------------------")

        contador_paginas += 1
        if contador_paginas > num_paginas:
            break
        pregunta_usuario_si_quiere_mas_recomendaciones = input("¿Quieres más recomendaciones? (S/N):    ")
        if pregunta_usuario_si_quiere_mas_recomendaciones.upper() == "N":
            break


def comprueba_que_existe_pelicula(json_respuesta_id_pelicula):
    num_resultados = json_respuesta_id_pelicula["total_results"]
    if num_resultados == 0:
        print("No existen películas con dicho nombre.")
        sys.exit(0)


if __name__ == '__main__':
    muestra_recomendaciones_de_peliculas()
