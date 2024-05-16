import os
import platform

def cleanConsole():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrarItems(listaItems):
    contador = 1
    for i in listaItems:
        print(f"{contador}. {i}")
        contador += 1

def ingresarOpcion(lista):
    mostrarItems(lista)
    while True:
        try:
            opcion = int(input("Seleccione producto (0 para salir): "))
            if 0 <= opcion <= len(lista):
                return opcion
            else:
                print(f"Productos: 1-{len(lista)} o 0 para salir")
        except ValueError:
            print("Ingrese producto (1-5) o 0 para salir")

def ingresarInt():
    while True:
        try:
            opcion = int(input(f"Ingrese la cantidad "))
            if opcion > 0:
                return opcion
            else:
                print(f"Tiene que ser mayor a 0")
        except ValueError:
            print("Ingrese un entero")

def verificarProducto(facturaElectronica, item):
    httpCode = facturaElectronica.add_items(item)

    if httpCode == "200":
        print("Producto agregado correctamente")
        return True
    else:
        print("No se pueden agregar más productos")
        facturaElectronica.showInfo()
        return False

