"""
        Programa con menú con el que se puede consultar mediante una Api acerca de películas.
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

from programas.apartados_get.get_codigo_de_pelicula import muestra_id_pelicula
from programas.apartados_get.get_generos_de_peliculas import muestra_generos_disponibles
from programas.apartados_get.get_informacion_pelicula import muestra_info_de_pelicula
from programas.apartados_get.get_trending import muestra_tt
from programas.apartados_get.get_peliculas_a_recomendar import muestra_recomendaciones_de_peliculas
from programas.menu.menu import Menu

SALIDA_DEL_PROGRAMA_CON_EXITO = 0

menu_cartelera = Menu("CARTELERA",
             "Buscar el código de una película.",
             "Buscar información de una película a partir de su código.",
             "Películas recomendadas a partir de tu película favorita.",
             "Obtener 5 películas trending topic.",
             "Mostrar géneros disponibles."
                      )

while True:
    option = menu_cartelera.escoger()
    match option:

        case 1:
            muestra_id_pelicula()
        case 2:
            muestra_info_de_pelicula()

        case 3:
            muestra_recomendaciones_de_peliculas()

        case 4:
            muestra_tt()

        case 5:
            muestra_generos_disponibles()

        case 6:
            print("¡Hasta la próxima ^_^!")
            sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
        case _:
            print("Ha introducido una opcion incorrecta, vuelva a intentarlo.")
