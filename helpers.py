import os
import platform
import re


def limpiar_pantalla():

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def leer_texto(longitud_min=1, longitud_max=50, mensaje=None):
    
    if mensaje:
        print(mensaje)

    while True:
        texto = input("> ")

        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def curp_valido(curp, lista_personas):
    
    expresion = r"^[A-Za-z]{4}\d{2}$"

    for persona in lista_personas:
        if persona.curp == curp:
            print("El curp que intentas ingresar ya ha sido registrado...")
            return False

    if re.match(expresion, curp):
        return True
    else:
        print("El curp ingresado no cumple con los requisitos...")
        return False
