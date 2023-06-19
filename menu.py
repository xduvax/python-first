import os
import database as db
import helpers
import menu_opciones as opciones

def inicio():
    
    while True:

        os.system("cls")
        print("======================")
        print("Bienvenido al programa")
        print("======================")
        print("\n[1] Listar personas")
        print("[2] Añadir persona")
        print("[3] Buscar persona")
        print("[4] Modificar persona")
        print("[5] Borrar persona")
        print("[6] Salir del programa")
        print("\n======================")

        opcion = input("\n\n>")

        if opcion == "1":
            opciones.listar_personas()

        elif opcion == "2":
            opciones.añadir_persona()
            
        elif opcion == "3":
            opciones.buscar_persona()

        elif opcion == "4":
            opciones.modificar_persona()

        elif opcion == "5":
            opciones.borrar_persona()

        elif opcion == "6":
            print("Saliendo del programa...")
            break
    
        input("\nPresiona enter para continuar")
