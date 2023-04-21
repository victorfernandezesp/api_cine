"""
        Programa con menu con el que se puede consultar mediante una Api acerca de películas.
        Se ha utilizado la API de TMDB.

        Entre las consultas disponibles se encuentran:
            *   Buscar el código de una película.
            *   Buscar información de una película.
            *   Películas recomendadas a partir de tu película favorita.
            *   Obtener 5 películas trending topic.
            *   Mostrar géneros disponibles.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
import sys

from programas.apartados_get.get_codigo_de_pelicula import get_codigo_pelicula
from programas.apartados_get.get_generos_de_peliculas import get_generos_pelicula
from programas.apartados_get.get_informacion_pelicula import get_informacion_pelicula
from programas.apartados_get.get_peliculas_a_recomendar import get_recomendar_pelicula
from programas.menu.menu import Menu

SALIDA_DEL_PROGRAMA_CON_EXITO = 0

menu_cartelera = Menu("CARTELERA",
             "Buscar el código de una película.",
             "Buscar información de una película.",
             "Películas recomendadas a partir de tu película favorita.",
             "Obtener 5 películas trending topic.",
             "Mostrar géneros disponibles."
                      )

while True:
    option = menu_cartelera.escoger()
    match option:

        case 1:
            get_codigo_pelicula()
        case 2:
            get_informacion_pelicula()

        case 3:
            get_recomendar_pelicula()

        case 4:
            pass

        case 5:
            get_generos_pelicula()

        case 6:
            sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
        case _:
            print("Ha introducido una opcion incorrecta, vuelva  a intentarlo.")
