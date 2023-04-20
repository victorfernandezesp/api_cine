"""
    En este programa se pretende: Buscar código de película según su nombre.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

def get_codigo_pelicula():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests

    API_KEY = credenciales.API_KEY
    contador_paginas = 1
    contador_peliculas = 0

    pelicula = input("¿De qué película quieres saber su código?:    ")

    # Se realiza la petición al servidor para obtener el número de páginas que tiene la consulta realizada
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}"
    params = {"query": {pelicula}, "language": "es-ES", "page": {contador_paginas}}
    respuesta_del_servidor = requests.get(url, params=params)
    json_respuesta = respuesta_del_servidor.json()

    num_paginas = json_respuesta["total_pages"]

    while True:
        # Se realiza la petición al servidor para obtener la información que se quiere obtener
        params = {"query": {pelicula}, "language": "es-ES", "page": {contador_paginas}}
        respuesta_del_servidor = requests.get(url, params=params)
        json_respuesta = respuesta_del_servidor.json()

        numero_de_pelis_por_pagina = len(json_respuesta["results"])

        for j in range(numero_de_pelis_por_pagina):
            titulo = json_respuesta["results"][j]["title"]
            id_pelicula = json_respuesta["results"][j]["id"]
            ano_de_lanzamiento = json_respuesta["results"][j]["release_date"]
            print("\n ID: {:<10} | Año de lanzamiento: {:<10} | Título: {:<60}".format(id_pelicula, ano_de_lanzamiento[:4], titulo))
            contador_peliculas += 1

        if contador_paginas == num_paginas:
            break
        pregunta_usuario_si_quiere_mas_peliculas = input("\n ¿Quieres más películas? (S/N):    \n")
        if pregunta_usuario_si_quiere_mas_peliculas.upper() == "N":
            break
        contador_paginas += 1

if __name__ == '__main__':
    get_codigo_pelicula()
