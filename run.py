import menu
import database as db

if __name__ == "__main__":
    db.ListaPersonas.cargar_datos()
    menu.inicio()
