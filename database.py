import csv
import config

class Persona:

    def __init__(self, curp, nombre, apellido, edad, correo):
        self.curp = curp
        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad
        self.correo = correo

    def __str__(self):
        return f"{self.curp} - {self.nombre} {self.apellido}, {self.edad} años... {self.correo}"

    
class ListaPersonas:

    lista = []

    @staticmethod
    def cargar_datos():

        with open(config.DATABASE_PATH, "r", newline="\n") as archivo:
            reader = csv.reader(archivo, delimiter=";")

            for curp, nombre, apellido, edad, correo in reader:
                persona = Persona(curp, nombre, apellido, edad, correo)
                ListaPersonas.lista.append(persona)

    @staticmethod
    def guardar_datos():
        
        with open(config.DATABASE_PATH, "w", newline="\n") as archivo:
            writer = csv.writer(archivo, delimiter=";")

            for persona in ListaPersonas.lista:
                writer.writerow( (persona.curp, persona.nombre, persona.apellido, persona.edad, persona.correo) )


    @staticmethod
    def crear(curp, nombre, apellido, edad, correo):

        persona = Persona(curp, nombre, apellido, edad, correo)
        ListaPersonas.lista.append(persona)
        ListaPersonas.guardar_datos()
        return persona


    @staticmethod
    def buscar(curp):
        
        for persona in ListaPersonas.lista:
            if persona.curp == curp:
                return persona

    @staticmethod
    def modificar(curp, nombre, apellido, edad, correo):

        for indice, persona in enumerate(ListaPersonas.lista):
            if persona.curp == curp:
                ListaPersonas.lista[indice].nombre = nombre
                ListaPersonas.lista[indice].apellido = apellido
                ListaPersonas.lista[indice].edad = edad
                ListaPersonas.lista[indice].correo = correo
                ListaPersonas.guardar_datos()
                return ListaPersonas.lista[indice]

    @staticmethod
    def borrar(curp):

        for indice, persona in enumerate(ListaPersonas.lista):
            if persona.curp == curp:
                borrada = ListaPersonas.lista.pop(indice)
                ListaPersonas.guardar_datos()
                return borrada
    