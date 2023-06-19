import unittest
import database as db
import copy
import helpers

class TestDatabase(unittest.TestCase):

    def setUp(self):

        db.ListaPersonas.lista = [
            db.Persona("DIGO88", "Oscar", "Diaz", 35, "ingoscardg@gmail.com"),
            db.Persona("FUDI13", "Isabella", "Fuentes", 12, "isabu@gmail.com"),
            db.Persona("ZIZU72", "Zinedine", "Zidane", 50, "zizu@gmail.com")
        ]

    # @classmethod
    # def tearDownClass(self):
    #     db.ListaPersonas.borrar("DIGO88")
    #     db.ListaPersonas.borrar("FUDI13")
    #     db.ListaPersonas.borrar("ZIZU72")

    def test_buscar_persona(self):

        cliente_existente = db.ListaPersonas.buscar("DIGO88")
        cliente_inexistente = db.ListaPersonas.buscar("XXXX75")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)
        self.assertEqual("Oscar", cliente_existente.nombre)

    def test_crear_persona(self):

        nuevo_cliente = db.ListaPersonas.crear("DIGO95", "Lisbet", "Hernandez", 24, "lisbet@gmail.com")
        self.assertEqual(4, len(db.ListaPersonas.lista))
        self.assertEqual("DIGO95", nuevo_cliente.curp)
        self.assertEqual("Lisbet", nuevo_cliente.nombre)
        self.assertEqual(24, nuevo_cliente.edad)

    def test_modificar_persona(self):

        copia_a_modificar = copy.copy(db.ListaPersonas.buscar("DIGO88"))
        copia_modificada = db.ListaPersonas.modificar("DIGO88", "Daniel", "Gonzalez", 38, "daniel@gmail.com")

        self.assertEqual("Oscar", copia_a_modificar.nombre)
        self.assertEqual("Daniel", copia_modificada.nombre)

    def test_borrar_persona(self):

        persona_buscada = db.ListaPersonas.buscar("DIGO88")
        self.assertEqual("Oscar", persona_buscada.nombre)
        db.ListaPersonas.borrar("DIGO88")
        self.assertIsNone(db.ListaPersonas.buscar("DIGO88"))

    def test_curp_valido(self):

        self.assertTrue( helpers.curp_valido("FUMA90", db.ListaPersonas.lista) )
        self.assertFalse( helpers.curp_valido("DIGO88", db.ListaPersonas.lista) )
        self.assertFalse( helpers.curp_valido("123456", db.ListaPersonas.lista) )
        self.assertFalse( helpers.curp_valido("aaaaaa", db.ListaPersonas.lista) )
        self.assertFalse( helpers.curp_valido("aaa123456", db.ListaPersonas.lista) )
        self.assertFalse( helpers.curp_valido("123456789", db.ListaPersonas.lista) )
