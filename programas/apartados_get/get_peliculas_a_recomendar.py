"""
    Apartado 3:
        Películas a recomendar si nos gusta una película concreta.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
def get_recomendar_pelicula():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests
    API_KEY = credenciales.API_KEY

    # Preguntamos al usuario la pelicula
    pelicula = input("Dime que pelicula te gusta y te recomendare varias más:    ")

    # Mandamos una petición al servidor y la almacenamos en Json

    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}"
    params = {"query": {pelicula}, "language": "es-ES"}
    respuesta_del_servidor_id_pelicula = requests.get(url, params=params)
    json_respuesta_id_pelicula = respuesta_del_servidor_id_pelicula.json()
    id_pelicula = json_respuesta_id_pelicula["results"][0]["id"]



    contador_paginas = 1
    url = f"https://api.themoviedb.org/3/movie/{id_pelicula}/recommendations?api_key={API_KEY}"

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
            print(f"{i+1}.  {pelicula_recomendada}")
            argumento = json_respuesta["results"][i]["overview"]
            print(f"    Trama argumental: \n {argumento} \n")

        print("\n-------------------------------------------------------------------------------------------------------------")

        contador_paginas += 1
        if contador_paginas > num_paginas:
            break
        pregunta_usuario_si_quiere_mas_recomendaciones = input("¿Quieres más recomendaciones? (S/N):    ")
        if pregunta_usuario_si_quiere_mas_recomendaciones.upper() == "N":
            break

if __name__ == '__main__':
    get_recomendar_pelicula()
