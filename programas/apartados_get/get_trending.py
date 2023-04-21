"""
    En este programa se pretende:  Encontrar las 5 películas "trending topic" semanal o del día y el género (concreto o todos)
    en función del usuario.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""


def muestra_tt():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests

    URL_BASE = "https://api.themoviedb.org/3/"
    API_KEY = credenciales.API_KEY

    contador_paginas = 1
    contador_peliculas = 0
    switch_elige_trending = False
    while True:
        trending = input("¿Deseas conocer el trending diario o semanal?(D/S):    ")
        if trending.upper() == "D":
            trending = "day"
            switch_elige_trending = True

        elif trending.upper() == "S":
            trending = "week"
            switch_elige_trending = True

        else:
            print("Debe responder con D/S")
            continue
        if switch_elige_trending:
            break

    switch_elige_genero = False
    while True:
        genero = input("¿Deseas un género concreto (S/N):    ")
        if genero.upper() == "S":
            genero_a_buscar =  input("¿Qúe genero deseas?:    ")
            URL_BASE = "https://api.themoviedb.org/3/"
            url = f"{URL_BASE}genre/movie/list?api_key={API_KEY}"
            params = {"language": "es-ES"}
            respuesta_del_servidor = requests.get(url, params=params)
            json_respuesta = respuesta_del_servidor.json()
            num_generos = len(json_respuesta["genres"])
            listado_generos = []
            for i in range(num_generos):
                generos_disponibles = json_respuesta["genres"][i]["name"]
                listado_generos.append(generos_disponibles)
            if genero_a_buscar in listado_generos:
                genero = genero_a_buscar
                switch_elige_genero = True
            else:
                print(f"{genero_a_buscar} no es un género disponible/válido")
                continue
            if switch_elige_genero:
                break
        else:
            """ge"""


    """# Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
    url = f"{URL_BASE}search/movie?api_key={API_KEY}"
    params = {"query": {pelicula}, "language": "es-ES", "page": {contador_paginas}}
    respuesta_del_servidor = requests.get(url, params=params)
    json_respuesta = respuesta_del_servidor.json()

    num_paginas = json_respuesta["total_pages"]

    comprueba_que_existen_resultados(json_respuesta)

    while True:
        # Se realiza la petición al servidor para obtener la información que se quiere obtener
        params = {"query": {pelicula}, "language": "es-ES", "page": {contador_paginas}}
        respuesta_del_servidor = requests.get(url, params=params)
        json_respuesta = respuesta_del_servidor.json()

        numero_de_pelis_por_pagina = len(json_respuesta["results"])
        # Se saca la información de las películas, se almacena y se muestra
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
        contador_paginas += 1"""


if __name__ == '__main__':
    muestra_tt()
