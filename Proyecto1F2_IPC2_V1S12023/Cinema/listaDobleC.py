import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import datetime

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazadaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            nuevo_nodo.siguiente = self.primero
            self.ultimo.siguiente = nuevo_nodo
            self.primero.anterior = nuevo_nodo
            self.ultimo = nuevo_nodo

    def obtener_lista_peliculas(self):
        lista_peliculas = []

        if self.primero is None:
            return lista_peliculas

        actual = self.primero
        while True:
            pelicula = {
                'titulo': actual.dato.titulo,
                'director': actual.dato.director,
                'año_pelicula': actual.dato.año_pelicula,
                'fecha_funcion': actual.dato.fecha_funcion,
                'hora_funcion': actual.dato.hora_funcion,
                'imagen': actual.dato.imagen,
                'precio': actual.dato.precio,
            }
            lista_peliculas.append(pelicula)
            actual = actual.siguiente
            if actual == self.primero:
                break

        return lista_peliculas
    
    def guardar_en_xml(self):
        root = ET.Element("categorias")

        categorias = set()
        actual = self.primero  # Reemplazar self.cabeza por self.primero
        while True:
            categoria = actual.dato.nombre_categoria
            categorias.add(categoria)
            actual = actual.siguiente
            if actual == self.primero:  # Reemplazar self.cabeza por self.primero
                break

        for categoria in categorias:
            categoria_element = ET.SubElement(root, "categoria")
            nombre_element = ET.SubElement(categoria_element, "nombre")
            nombre_element.text = categoria

            peliculas_element = ET.SubElement(categoria_element, "peliculas")

            actual = self.primero  # Reemplazar self.cabeza por self.primero
            while True:
                if actual.dato.nombre_categoria == categoria:
                    pelicula_element = ET.SubElement(peliculas_element, "pelicula")

                    titulo_element = ET.SubElement(pelicula_element, "titulo")
                    titulo_element.text = actual.dato.titulo

                    director_element = ET.SubElement(pelicula_element, "director")
                    director_element.text = actual.dato.director

                    anio_element = ET.SubElement(pelicula_element, "anio")
                    anio_element.text = str(actual.dato.año_pelicula)

                    fecha_element = ET.SubElement(pelicula_element, "fecha")
                    fecha_element.text = datetime.strptime(actual.dato.fecha_funcion, "%Y-%m-%d").strftime("%Y-%m-%d")

                    hora_element = ET.SubElement(pelicula_element, "hora")
                    hora_element.text = datetime.strptime(actual.dato.hora_funcion, "%H:%M").strftime("%H:%M")

                    imagen_element = ET.SubElement(pelicula_element, "imagen")
                    imagen_element.text = actual.dato.imagen.name if actual.dato.imagen else ""

                    precio_element = ET.SubElement(pelicula_element, "precio")
                    precio_element.text = str(actual.dato.precio)

                actual = actual.siguiente
                if actual == self.primero:  # Reemplazar self.cabeza por self.primero
                    break

        tree = ET.ElementTree(root)
        tree.write("peliculas.xml")