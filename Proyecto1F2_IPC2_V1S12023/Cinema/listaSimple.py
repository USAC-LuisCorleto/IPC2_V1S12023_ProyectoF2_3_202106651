import xml.etree.ElementTree as ET
from .models import Usuario

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def buscar_usuario(self, correo, contraseña):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.correo == correo and actual.dato.contraseña == contraseña:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def generar_archivo_XML(self, archivo=None):
        root = ET.Element("usuarios")
        actual = self.cabeza

        while actual is not None:
            usuario_element = ET.SubElement(root, "usuario")

            rol_element = ET.SubElement(usuario_element, "rol")
            rol_element.text = actual.dato.rol

            nombre_element = ET.SubElement(usuario_element, "nombre")
            nombre_element.text = actual.dato.nombre

            apellido_element = ET.SubElement(usuario_element, "apellido")
            apellido_element.text = actual.dato.apellido

            telefono_element = ET.SubElement(usuario_element, "telefono")
            telefono_element.text = actual.dato.telefono

            correo_element = ET.SubElement(usuario_element, "correo")
            correo_element.text = actual.dato.correo

            contraseña_element = ET.SubElement(usuario_element, "contrasena")
            contraseña_element.text = actual.dato.contraseña

            actual = actual.siguiente

        tree = ET.ElementTree(root)

        if archivo:
            tree.write(archivo)
        else:
            tree.write("usuarios.xml")

    def obtener_lista_usuarios(self):
        lista_usuarios = []

        actual = self.cabeza
        while actual is not None:
            usuario = {
                'rol': actual.dato.rol,
                'nombre': actual.dato.nombre,
                'apellido': actual.dato.apellido,
                'telefono': actual.dato.telefono,
                'correo': actual.dato.correo,
                'contraseña': actual.dato.contraseña,
            }
            lista_usuarios.append(usuario)
            actual = actual.siguiente

        return lista_usuarios
    
    def actualizar_usuario(self, correo, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.correo == correo:
                actual.dato.nombre = nuevo_nombre
                actual.dato.apellido = nuevo_apellido
                actual.dato.telefono = nuevo_telefono
                actual.dato.contraseña = nueva_contrasena
                break
            actual = actual.siguiente

        tree = ET.parse('usuarios.xml')
        root = tree.getroot()

        for usuario_element in root.findall('usuario'):
            if usuario_element.find('correo').text == correo:
                usuario_element.find('nombre').text = nuevo_nombre
                usuario_element.find('apellido').text = nuevo_apellido
                usuario_element.find('telefono').text = nuevo_telefono
                usuario_element.find('contrasena').text = nueva_contrasena

        tree.write('usuarios.xml')

    def eliminar_usuario(self, correo):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.dato.correo == correo:
                break
            anterior = actual
            actual = actual.siguiente
        if actual is not None:
            if anterior is None:
                self.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
        tree = ET.parse('usuarios.xml')
        root = tree.getroot()

        for usuario_element in root.findall('usuario'):
            if usuario_element.find('correo').text == correo:
                root.remove(usuario_element)

        tree.write('usuarios.xml')
    
    def cargar_desde_xml(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        for usuario_element in root.findall('.//usuario'):
            rol = usuario_element.find('rol').text
            nombre = usuario_element.find('nombre').text
            apellido = usuario_element.find('apellido').text
            telefono = usuario_element.find('telefono').text
            correo = usuario_element.find('correo').text
            contraseña = usuario_element.find('contrasena').text

            usuario = Usuario(rol=rol, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, contraseña=contraseña)
            self.add(usuario)

