"""
    En este programa se pretende:  Encontrar las 5 películas "trending topic" semanal o del día y el género (concreto o todos)
    en función del usuario.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

NUMERO_PELIS_A_MOSTRAR = 5


def muestra_tt():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests

    URL_BASE = "https://api.themoviedb.org/3/"
    API_KEY = credenciales.API_KEY

    contador_paginas = 1
    id_genero = 0
    trending = pregunta_trending_diario_semanal()

    while True:
        genero = input("¿Deseas un género concreto (S/N):    ")
        if genero.upper() == "S":
            while True:
                """ Si desea un género concreto realizamos una petición al servidor, almacenamos el número de géneros 
                    existentes, almacenamos el íd de géneros y creamos dos listas para identificar cada género con su
                    código además se comprueba que exista ese género, si el usuario no desea un género concreto pasamos y
                    asignamos el género como una N. """

                genero_a_buscar =  input("¿Qúe género deseas?:    ")
                url = f"{URL_BASE}genre/movie/list?api_key={API_KEY}"
                params = {"language": "es-ES"}
                try:
                    respuesta_del_servidor = requests.get(url, params=params)
                except ConnectionError:
                    print("No tienes conexión a internet, vuelve a intentarlo cuando tengas conexión. ")
                    sys.exit(1)
                json_respuesta = respuesta_del_servidor.json()
                num_generos = len(json_respuesta["genres"])
                listado_generos = []
                listado_id = []
                for i in range(num_generos):
                    generos_disponibles = json_respuesta["genres"][i]["name"]
                    listado_generos.append(generos_disponibles)
                    id_generos_disponibles = json_respuesta["genres"][i]["id"]
                    listado_id.append(id_generos_disponibles)
                if genero_a_buscar in listado_generos:
                    posicion_id = listado_generos.index(genero_a_buscar)
                    genero = genero_a_buscar
                    id_genero = listado_id[posicion_id]
                    break
                else:
                    print(f"{genero_a_buscar} no es un género disponible/válido")
                    continue
            break
        elif genero.upper() == "N":
            break
        else:
            print("Debes responder con S/N")
            continue

    """ Si el género es N significa que al usuario le da igual el género, se procede a hacer una petición al servidor 
        donde se sacan las 5 primeras peliculas TT diarias o semanales. """

    if genero.upper() == "N":
        # Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
        url = f"{URL_BASE}/trending/movie/{trending}?api_key={API_KEY}"
        params = {"language": "es-ES"}
        try:
            respuesta_del_servidor = requests.get(url, params=params)
        except ConnectionError:
            print("No tienes conexión a internet, vuelve a intentarlo cuando tengas conexión. ")
            sys.exit(1)
        json_respuesta = respuesta_del_servidor.json()

        for j in range(NUMERO_PELIS_A_MOSTRAR):
            titulo = json_respuesta["results"][j]["title"]
            id_pelicula = json_respuesta["results"][j]["id"]
            ano_de_lanzamiento = json_respuesta["results"][j]["release_date"]
            valoracion_media = json_respuesta["results"][j]["vote_average"]
            numero_votos = json_respuesta["results"][j]["vote_count"]
            print("\n ID: {:<10} | Valoración: {:<10} | Votos: {:<10} | Año de lanzamiento: {:<10} | Título: {:<60}".format(id_pelicula, valoracion_media, numero_votos, ano_de_lanzamiento[:4], titulo))


    else:

        """ Por el contrario, si se llega hasta aquí significa que el género es uno concreto dictaminado por el usuario 
        y que además existe, viene recogido en la lista con todos los géneros, hacemos una petición al servidor, en el 
        primer while servirá para pasar de página en caso de no encontrar mas títulos con dicho género.
        El for j nos servirá para comprobar cada película de la pagina X y si coincide el mismo género entonces 
        mostrarlo y aumentar en 1 el contador de películas."""

        contador_peliculas = 0
        while True:
            # Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
            url = f"{URL_BASE}/trending/movie/{trending}?api_key={API_KEY}"
            params = {"language": "es-ES", "page": {contador_paginas}}
            try:
                respuesta_del_servidor = requests.get(url, params=params)
            except ConnectionError:
                print("No tienes conexión a internet, vuelve a intentarlo cuando tengas conexión. ")
                sys.exit(1)
            json_respuesta = respuesta_del_servidor.json()
            num_pelis_en_pagina = len(json_respuesta["results"])

            for j in range(num_pelis_en_pagina):
                titulo = json_respuesta["results"][j]["title"]
                id_pelicula = json_respuesta["results"][j]["id"]
                ano_de_lanzamiento = json_respuesta["results"][j]["release_date"]
                valoracion_media = json_respuesta["results"][j]["vote_average"]
                longitud_generos_de_pelicula_concreta = len(json_respuesta["results"][j]["genre_ids"])
                numero_votos = json_respuesta["results"][j]["vote_count"]
                lista_generos_de_pelicula_concreta = []
                for k in range(longitud_generos_de_pelicula_concreta):
                    lista_generos_de_pelicula_concreta.append(json_respuesta["results"][j]["genre_ids"][k])
                if id_genero in lista_generos_de_pelicula_concreta:
                    print("\n ID: {:<10} | Valoración: {:<10} | Votos: {:<10} | Año de lanzamiento: {:<10} | Título: {:<60}".format(
                            id_pelicula, valoracion_media, numero_votos, ano_de_lanzamiento[:4], titulo))

                    contador_peliculas += 1
                    if contador_peliculas == NUMERO_PELIS_A_MOSTRAR:
                        break
            if contador_peliculas == NUMERO_PELIS_A_MOSTRAR:
                break
            contador_paginas += 1


def pregunta_trending_diario_semanal():
    while True:
        trending = input("¿Deseas conocer el trending diario o semanal?(D/S):    ")
        if trending.upper() == "D":
            trending = "day"
            return trending
        elif trending.upper() == "S":
            trending = "week"
            return trending
        else:
            print("Debe responder con D/S")
            continue



if __name__ == '__main__':
    muestra_tt()
