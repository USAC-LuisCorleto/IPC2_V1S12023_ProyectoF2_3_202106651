import xml.etree.ElementTree as ET

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.anterior.siguiente = nuevo_nodo
    
    def guardar_en_xml(self):
        root = ET.Element("cines")

        cine_element = ET.SubElement(root, "cine")
        nombre_element = ET.SubElement(cine_element, "nombre")
        nombre_element.text = "Cinepolis"  # Establecer el nombre del cine

        salas_element = ET.SubElement(cine_element, "salas")

        actual = self.primero
        while actual is not None:
            sala_actual = actual.dato

            sala_element = ET.SubElement(salas_element, "sala")

            numero_element = ET.SubElement(sala_element, "numero")
            numero_element.text = sala_actual.numero_sala

            asientos_element = ET.SubElement(sala_element, "asientos")
            asientos_element.text = str(sala_actual.capacidad)

            actual = actual.siguiente

        tree = ET.ElementTree(root)
        tree.write("salas.xml")

    