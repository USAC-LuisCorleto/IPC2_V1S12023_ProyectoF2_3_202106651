import xml.etree.ElementTree as ET
from .models import Tarjeta

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazadaT:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def generar_archivo_xml(self):
        raiz = ET.Element("tarjetas")

        nodo_actual = self.primero
        while nodo_actual:
            tarjeta = ET.SubElement(raiz, "tarjeta")

            tipo = ET.SubElement(tarjeta, "tipo")
            tipo.text = nodo_actual.dato.tipo

            numero = ET.SubElement(tarjeta, "numero")
            numero.text = nodo_actual.dato.numero

            titular = ET.SubElement(tarjeta, "titular")
            titular.text = nodo_actual.dato.titular

            fecha_expiracion = ET.SubElement(tarjeta, "fecha_expiracion")
            fecha_expiracion.text = nodo_actual.dato.fecha_expiracion

            nodo_actual = nodo_actual.siguiente

        arbol = ET.ElementTree(raiz)
        arbol.write("tarjetas.xml")

    def obtener_lista_tarjetas(self):
        lista_salas = []

        actual = self.primero
        while actual is not None:
            tarjeta = {
                'tipo': actual.dato.tipo,
                'numero': actual.dato.numero,
                'titular': actual.dato.titular,
                'fecha_expiracion': actual.dato.fecha_expiracion,
            }
            lista_salas.append(tarjeta)
            actual = actual.siguiente

        return lista_salas
    
    def actualizar_tarjeta(self, numero_tarjeta, nuevo_numero, nuevo_titular, nueva_fecha_expiracion):
        actual = self.primero
        while actual is not None:
            if actual.dato.numero == numero_tarjeta:
                actual.dato.numero = nuevo_numero
                actual.dato.titular = nuevo_titular
                actual.dato.fecha_expiracion = nueva_fecha_expiracion
                break
            actual = actual.siguiente

        tree = ET.parse('tarjetas.xml')
        root = tree.getroot()

        for tarjeta_element in root.findall('.//tarjeta'):
            if tarjeta_element.find('numero').text == numero_tarjeta:
                tarjeta_element.find('numero').text = nuevo_numero
                tarjeta_element.find('titular').text = nuevo_titular
                tarjeta_element.find('fecha_expiracion').text = nueva_fecha_expiracion

        tree.write('tarjetas.xml')

    def eliminar_tarjeta(self, numero_tarjeta):
        actual = self.primero
        while actual is not None:
            if actual.dato.numero == numero_tarjeta:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior

                break
            actual = actual.siguiente

        tree = ET.parse('tarjetas.xml')
        root = tree.getroot()

        for tarjeta_element in root.findall('.//tarjeta'):
            if tarjeta_element.find('numero').text == numero_tarjeta:
                root.remove(tarjeta_element)
                break

        tree.write('tarjetas.xml')

    def cargar_desde_xml(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        for tarjeta_element in root.findall('.//tarjeta'):
            tipo = tarjeta_element.find('tipo').text
            numero = tarjeta_element.find('numero').text
            titular = tarjeta_element.find('titular').text
            fecha_expiracion = tarjeta_element.find('fecha_expiracion').text

            tarjeta = Tarjeta(tipo=tipo, numero=numero, titular=titular, fecha_expiracion=fecha_expiracion)
            self.agregar(tarjeta)