"""Zaimplementuj mechanizm automatycznego generowania kolejnych ID dla produktów.
Informację o kolejnym ID przechowuj jako pole klasowe (class attribute).

Przykład użycia:
> product_1 = Product('Woda', 1.99)
> product_1.id
1
> product_2 = Product('Chleb', 2.50)
> product_2.id
2"""

class Product:
    ID = 0

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @staticmethod
    def id():
        Product.ID += 1
        id = Product.ID
        return print(id)

product_1 = Product('Woda', 1.99)
product_1.id()
product_2 = Product('Chleb', 2.50)
product_2.id()