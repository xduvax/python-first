import database as db
import helpers

def listar_personas():

    print("Listando personal...\n")

    for persona in db.ListaPersonas.lista:
        print(persona)


def añadir_persona():

    print("Añadiendo persona...\n")
    while True:
        
        curp = helpers.leer_texto(6, 6, "CURP: 6 caracteres - 4 CHAR 2 INT").upper()
        if helpers.curp_valido(curp, db.ListaPersonas.lista):
            break
        
    nombre = helpers.leer_texto(2, 20, "Nombre: de 2 a 20 caracteres").capitalize()
    apellido = helpers.leer_texto(2, 20, "Apellido: de 2 a 20 caracteres").capitalize()
    edad = int(helpers.leer_texto(2,2, "Edad: INT menor a 100"))
    correo = helpers.leer_texto(5, 30, "Correo: ")
    creado = db.ListaPersonas.crear(curp, nombre, apellido, edad, correo)

    if creado:
        print("\nPersona añadida correctamente...")


def buscar_persona():

    print("Buscando persona...\n")

    curp = helpers.leer_texto(6, 6, "CURP: 6 caracteres - 4 CHAR 2 INT").upper()
    persona = db.ListaPersonas.buscar(curp)

    if persona:
        print(persona)
    else:
        print("Persona no encontrada")


def modificar_persona():
    
    print("Modificando persona...\n")

    curp = helpers.leer_texto(6, 6, "CURP: 6 caracteres - 4 CHAR 2 INT").upper()
    persona = db.ListaPersonas.buscar(curp)
    if persona:
        nombre = helpers.leer_texto(2, 20, f"Nombre: de 2 a 20 caracteres -  [{persona.nombre}]").capitalize()
        apellido = helpers.leer_texto(2, 20, f"Apellido: de 2 a 20 caracteres - [{persona.apellido}]").capitalize()
        edad = int(helpers.leer_texto(2, 2, f"Edad: INT menor a 100 - [{persona.edad}]"))
        correo = helpers.leer_texto(5, 30, f"Correo, STRING - [{persona.correo}]")
        modificada = db.ListaPersonas.modificar(curp, nombre, apellido, edad, correo)

        if modificada:
            print("Persona modificada correctamente")
        else:
            print("Hubo un error...")
    else:
        print("CURP no encontrado")
        

def borrar_persona():

    print("Borrando persona...\n")

    curp = helpers.leer_texto(6, 6, "CURP: 6 caracteres - 4 CHAR 2 INT").upper()
    if db.ListaPersonas.borrar(curp):
        print("Persona borrada correctamente...")
    else:
        print("Persona no encontrada")
