import xml.etree.ElementTree as ET
from datetime import datetime
from datetime import datetime
from .models import Película

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
        actual = self.primero
        while True:
            categoria = actual.dato.nombre_categoria
            categorias.add(categoria)
            actual = actual.siguiente
            if actual == self.primero: 
                break

        for categoria in categorias:
            categoria_element = ET.SubElement(root, "categoria")
            nombre_element = ET.SubElement(categoria_element, "nombre")
            nombre_element.text = categoria

            peliculas_element = ET.SubElement(categoria_element, "peliculas")

            actual = self.primero 
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
                if actual == self.primero:  
                    break

        tree = ET.ElementTree(root)
        tree.write("peliculas.xml")

    def actualizar_pelicula(self, titulo, nuevo_director, nuevo_año_pelicula, nueva_fecha_funcion, nueva_hora_funcion, nuevo_precio):
        actual = self.primero
        while True:
            if actual.dato.titulo == titulo:
                actual.dato.titulo == titulo
                actual.dato.director = nuevo_director
                actual.dato.año_pelicula = nuevo_año_pelicula
                actual.dato.fecha_funcion = nueva_fecha_funcion
                actual.dato.hora_funcion = nueva_hora_funcion
                actual.dato.precio = nuevo_precio
                break
            actual = actual.siguiente
            if actual == self.primero:
                break

        tree = ET.parse('peliculas.xml')
        root = tree.getroot()

        for pelicula_element in root.findall('.//pelicula'):
            if pelicula_element.find('titulo').text == titulo:
                pelicula_element.find('director').text = nuevo_director
                pelicula_element.find('anio').text = str(nuevo_año_pelicula)
                pelicula_element.find('fecha').text = datetime.strptime(nueva_fecha_funcion, "%Y-%m-%d").strftime("%Y-%m-%d")
                pelicula_element.find('hora').text = datetime.strptime(nueva_hora_funcion, "%H:%M").strftime("%H:%M")
                pelicula_element.find('precio').text = str(nuevo_precio)

        tree.write('peliculas.xml')

    def cargar_desde_xml(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        for categoria_element in root.findall('.//categoria'):
            nombre_categoria = categoria_element.find('nombre').text

            peliculas_element = categoria_element.find('peliculas')

            for pelicula_element in peliculas_element.findall('pelicula'):
                titulo = pelicula_element.find('titulo').text
                director = pelicula_element.find('director').text
                año_pelicula = int(pelicula_element.find('anio').text)
                fecha_funcion = pelicula_element.find('fecha').text
                hora_funcion = pelicula_element.find('hora').text
                
                imagen_element = pelicula_element.find('imagen')
                imagen = imagen_element.text if imagen_element is not None else None

                precio_element = pelicula_element.find('precio')
                precio = float(precio_element.text) if precio_element is not None else 0.0

                pelicula = Película(
                    nombre_categoria=nombre_categoria,
                    titulo=titulo,
                    director=director,
                    año_pelicula=año_pelicula,
                    fecha_funcion=fecha_funcion,
                    hora_funcion=hora_funcion,
                    imagen=imagen,
                    precio=precio
                )

                self.add(pelicula)
        
    def eliminar_pelicula(self, titulo):
        if self.primero is None:
            return

        actual = self.primero
        while True:
            if actual.dato.titulo == titulo:
                if actual == self.primero:
                    self.primero = actual.siguiente
                if actual == self.ultimo:
                    self.ultimo = actual.anterior

                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior

                # Eliminar el objeto película si es necesario
                del actual.dato
                del actual

                break

            actual = actual.siguiente
            if actual == self.primero:
                break
            
    def eliminar_pelicula_del_xml(self, titulo):
        tree = ET.parse('peliculas.xml')
        root = tree.getroot()

        for categoria_element in root.findall('.//categoria'):
            peliculas_element = categoria_element.find('peliculas')

            for pelicula_element in peliculas_element.findall('pelicula'):
                if pelicula_element.find('titulo').text == titulo:
                    peliculas_element.remove(pelicula_element)

        tree.write('peliculas.xml')
