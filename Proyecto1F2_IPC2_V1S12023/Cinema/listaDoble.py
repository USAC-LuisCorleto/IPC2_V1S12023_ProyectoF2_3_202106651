import xml.etree.ElementTree as ET
from .models import Sala

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

    def obtener_lista_salas(self):
        lista_salas = []

        actual = self.primero
        while actual is not None:
            sala = {
                'numero_sala': actual.dato.numero_sala,
                'capacidad': actual.dato.capacidad,
            }
            lista_salas.append(sala)
            actual = actual.siguiente

        return lista_salas

    def actualizar_sala(self, numero_sala, nueva_capacidad):
        actual = self.primero
        while actual is not None:
            if actual.dato.numero_sala == numero_sala:
                actual.dato.capacidad = nueva_capacidad
                break
            actual = actual.siguiente

        tree = ET.parse('salas.xml')
        root = tree.getroot()

        for sala_element in root.findall('.//sala'):
            if sala_element.find('numero').text == numero_sala:
                sala_element.find('asientos').text = str(nueva_capacidad)

        tree.write('salas.xml')

    def eliminar_sala(self, sala):
        actual = self.primero
        while actual is not None:
            if actual.dato.numero_sala == sala:
                break
            actual = actual.siguiente
        if actual is not None:
            if actual.anterior is None:
                self.primero = actual.siguiente
            else:
                actual.anterior.siguiente = actual.siguiente
            if actual.siguiente is not None:
                actual.siguiente.anterior = actual.anterior

            # Eliminar el elemento correspondiente del archivo XML
            tree = ET.parse('salas.xml')
            root = tree.getroot()

            for sala_element in root.findall('sala'):
                if sala_element.find('numero').text == sala:
                    root.remove(sala_element)

            tree.write('salas.xml')

        self.guardar_en_xml()

    def cargar_desde_xml(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        for sala_element in root.findall('.//sala'):
            numero_sala = sala_element.find('numero').text
            capacidad = int(sala_element.find('asientos').text)

            sala = Sala(numero_sala=numero_sala, capacidad=capacidad)
            self.add(sala)
