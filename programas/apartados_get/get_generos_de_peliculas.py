"""
    En este programa se pretende: Mostrar géneros disponibles.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""

def get_generos_pelicula():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests
    API_KEY = credenciales.API_KEY

    # Mandamos una petición al servidor y la almacenamos en Json
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
    params = {"language": "es-ES"}
    respuesta_del_servidor = requests.get(url, params=params)
    json_respuesta = respuesta_del_servidor.json()

    num_generos = len(json_respuesta["genres"])

    print("-------------------------------------------------------------------------------------------------------------\n")
    print(f"Los géneros disponibles:")
    for i in range(num_generos):
        generos_disponibles = json_respuesta["genres"][i]["name"]
        print(f"{i+1}.  {generos_disponibles}")

    print("\n-------------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    get_generos_pelicula()
