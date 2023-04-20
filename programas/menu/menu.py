"""
    Muestra un menú con las opciones introducidas por teclado.

    Autor: Víctor Fernández España
    Curso: 2022-2023
"""
from typeguard import typechecked


@typechecked
class Menu:
    def __init__(self, titulo: str, *opciones: str):
        self.__titulo = titulo
        self.__opciones = list(opciones)
        self.__opciones.append("Terminar")

    def __mostrar_opciones(self):
        print("\n*******************************************")
        print(f"********* BIENVENIDO A {self.__titulo} **********")
        print("*******************************************\n\n")
        print("Por favor, seleccione una opción: \n")
        contador = 1

        for opcion in self.__opciones:
            print(f"{contador}. {opcion}")
            contador += 1
        print("")

    def escoger(self):
        self.__mostrar_opciones()
        x = int(input("¿Que vas a seleccionar?    "))
        return x

    def __str__(self):
        return f"{self.__titulo}:{self.__opciones} "

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__titulo}:{self.__opciones} )"