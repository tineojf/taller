class Compra:
    def __init__(self, item, cantidad):
        self.producto = item
        self.cantidad = cantidad
        self.subtotal = self.calculateSubtotal()

    def calculateSubtotal(self):
        return self.producto.getPrice() * self.cantidad
    
    def getSubtotal(self):
        return self.subtotal

    def __str__(self):
        return f"{self.producto.getName()}: ${self.subtotal:.2f} (${self.producto.getPrice():.2f} x {self.cantidad})"
