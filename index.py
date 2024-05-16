from Item import Item
from funciones import *
from Factura import FacturaElectronica

factura = FacturaElectronica()
productos = [
    Item("Cámara de seguridad", 100),
    Item("Alarma contra incendios", 150),
    Item("Sensor de movimiento", 50),
    Item("Detector de humo", 80),
    Item("Cerradura electrónica", 120)
]

verificar = True
while verificar:
    opcion_elegida = ingresarOpcion(productos)
    if opcion_elegida == 0:
        cleanConsole()
        factura.showInfo()
        break
    verificar = verificarProducto(factura, productos[opcion_elegida - 1])
