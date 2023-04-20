"""
    Apartado 2:
        Buscar información de película según su código. Entre los datos de la información debe estar:
            Título.
            Géneros.
            Argumento.
            Duración.
            ...
            Y enlace a su web en IMDB.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
def get_informacion_pelicula():

    # Importamos Credenciales (Donde se carga la variable de entorno donde está la Api )
    import credenciales
    import requests
    API_KEY = credenciales.API_KEY

    # Preguntamos al usuario la pelicula
    codigo_de_pelicula = input("¿Dame el código de la película a buscar:    ")

    # Mandamos una petición al servidor y la almacenamos en Json
    url = f"https://api.themoviedb.org/3/movie/{codigo_de_pelicula}?api_key={API_KEY}"
    params = {"language": "es-ES"}
    respuesta_del_servidor = requests.get(url, params=params)
    json_respuesta = respuesta_del_servidor.json()

    print("-------------------------------------------------------------------------------------------------------------\n")
    titulo = json_respuesta["title"]
    print(f"La película con id: {codigo_de_pelicula} es: {titulo}. \n")

    print(f"Los géneros son:")
    num_generos = len(json_respuesta["genres"])
    for i in range(num_generos):
        genero = json_respuesta["genres"][i]["name"]
        print(f"{i+1}.  {genero}")

    argumento = json_respuesta["overview"]
    print(f"\n Trama argumental: \n {argumento} \n")

    duracion = json_respuesta["runtime"]
    horas = int(duracion) // 60
    minutos = int(duracion) % 60
    print(f"La duración de la pelicula es de: {horas} horas y {minutos} minutos. \n")

    id_imdb = json_respuesta["imdb_id"]
    print(f"La url a IMDb de la pelicula: https://www.imdb.com/title/{id_imdb}")

    print("\n-------------------------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    get_informacion_pelicula()