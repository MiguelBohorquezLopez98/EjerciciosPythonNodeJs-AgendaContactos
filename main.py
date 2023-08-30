import os
from conexion import *
from contacto import *

con = conectar()
crear_tabla(con)

def iniciar():
    os.system('clear')
    print('Seleccione una opción: ')
    print('\t1. Añadir un contacto')
    print('\t2. Mostrar todos los contactos')
    print('\t3. Buscar un contacto')
    print('\t4. Modificar un contacto')
    print('\t5. Eliminar un contacto')
    print('\t1. Salir de la aplicación')
    opcion = input('Escoja una opción: ')
    if opcion == '1':
        nuevo_contacto()
    # elif opcion == '2':
    #     mostrar_contactos()
    

    def nuevo_contacto():
        nombre = input('Ingrese el nombre: ')
        apellidos = input('Ingrese el apellido: ')
        empresa = input('Ingrese la empresa: ')
        telefono = input('Ingrese el telefono: ')
        email = input('Ingrese el email: ')
        direccion = input('Ingrese la direccion: ')
        respuesta = registrar(nombre, apellidos, empresa, telefono, email, direccion)
        print(respuesta)

iniciar()