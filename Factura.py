from Compra import Compra
from funciones import ingresarInt

class FacturaElectronica:
    def __init__(self):
        self.listaCompra = []
        self.subtotal = 0
        self.iva = 0.18

    def add_items(self, item):
        if len(self.listaCompra) < 10:
            cantidad = ingresarInt()
            compra = Compra(item, cantidad)

            self.subtotal += compra.getSubtotal()
            self.listaCompra.append(compra)
            return "200"
        else:
            return "401"

    def calculateTotal(self):
        return self.subtotal * (1 + self.iva)

    def showInfo(self):
        print("*************  Factura electronica  *************\n")
        print("Lista de ítems:")
        for i in self.listaCompra:
            print(i)
        
        print()
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"IVA: ${self.subtotal * self.iva:.2f}")
        print(f"Total: ${self.calculateTotal():.2f}")