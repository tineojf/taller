class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"
    
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price

