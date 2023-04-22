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

    genero = input("¿Deseas un género concreto (S/N):    ")
    if genero.upper() == "S":
        while True:
            genero_a_buscar =  input("¿Qúe genero deseas?:    ")
            URL_BASE = "https://api.themoviedb.org/3/"
            url = f"{URL_BASE}genre/movie/list?api_key={API_KEY}"
            params = {"language": "es-ES"}
            respuesta_del_servidor = requests.get(url, params=params)
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
    elif genero.upper() == "N":
        pass
    else:
        print("Debes responder con S/N")
        sys.exit(0)




    if genero.upper() == "N":
        # Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
        url = f"{URL_BASE}/trending/movie/{trending}?api_key={API_KEY}"
        params = {"language": "es-ES"}
        respuesta_del_servidor = requests.get(url, params=params)
        json_respuesta = respuesta_del_servidor.json()

        for j in range(NUMERO_PELIS_A_MOSTRAR):
            titulo = json_respuesta["results"][j]["title"]
            id_pelicula = json_respuesta["results"][j]["id"]
            ano_de_lanzamiento = json_respuesta["results"][j]["release_date"]
            print("\n ID: {:<10} | Año de lanzamiento: {:<10} | Título: {:<60}".format(id_pelicula, ano_de_lanzamiento[:4], titulo))

    else:
        contador_peliculas = 0
        while True:
            # Se realiza la petición al servidor y se guarda el Json que devuelve en una variable
            url = f"{URL_BASE}/trending/movie/{trending}?api_key={API_KEY}"
            params = {"language": "es-ES", "page": {contador_paginas}}
            respuesta_del_servidor = requests.get(url, params=params)
            json_respuesta = respuesta_del_servidor.json()
            num_pelis_en_pagina = len(json_respuesta["results"])

            for j in range(num_pelis_en_pagina):
                titulo = json_respuesta["results"][j]["title"]
                id_pelicula = json_respuesta["results"][j]["id"]
                ano_de_lanzamiento = json_respuesta["results"][j]["release_date"]
                longitud_generos_de_pelicula_concreta = len(json_respuesta["results"][j]["genre_ids"])
                lista_generos_de_pelicula_concreta = []
                for k in range(longitud_generos_de_pelicula_concreta):
                    lista_generos_de_pelicula_concreta.append(json_respuesta["results"][j]["genre_ids"][k])
                if id_genero in lista_generos_de_pelicula_concreta:
                    print("\n ID: {:<10} | Año de lanzamiento: {:<10} | Título: {:<60}".format(id_pelicula, ano_de_lanzamiento[:4], titulo))
                    contador_peliculas += 1
                    if contador_peliculas == NUMERO_PELIS_A_MOSTRAR:
                        break
            if contador_peliculas == NUMERO_PELIS_A_MOSTRAR:
                break
            contador_paginas += 1


def pregunta_trending_diario_semanal():
    trending = input("¿Deseas conocer el trending diario o semanal?(D/S):    ")
    if trending.upper() == "D":
        trending = "day"

    elif trending.upper() == "S":
        trending = "week"

    else:
        print("Debe responder con D/S")
        sys.exit(0)
    return trending


if __name__ == '__main__':
    muestra_tt()
