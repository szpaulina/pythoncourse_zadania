"""
Zaimplementuj metodę statyczną tworzącą koszyk na podstawie listy podanych produktów.
Każdy z nich powinien zostać dodany do koszyka tylko raz.
Przykład użycia:
backset = Basket.with_products([prod_1, prod_2])
"""

from collections import defaultdict

class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN'

    def __str__(self) -> str:
        return self.get_info()


class Basket:
    def __init__(self):
        self._items = defaultdict(int)

    def add_product(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("Product has to be an instance of class Product.")

        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        self._items[product] += quantity

    def count_total_price(self) -> float:
        return sum([product.price * quantity for product, quantity in self._items.items()])

    def generate_report(self):
        """
        Produkty w koszyku:
        - Woda (1), cena: 10.00 x 5
        W sumie: 50.00
        """
        print('Produkty w koszyku:')
        for product, quantity in self._items.items():
            print(f'- {product} x {quantity}')
        print(f'W sumie: {self.count_total_price():.2f} PLN')

    def product_count(self) -> int:
        return len(self._items)

    @property
    def is_empty(self) -> bool:
        if len(self._items) > 0:
            return False
        else:
            return True

    @staticmethod
    def with_products(lista: list):
        if not isinstance(lista, list):
            raise TypeError("Lista has to be an instance of list.")

        koszyk = Basket()

        for element in lista:
            if not isinstance(element, Product):
                raise TypeError("Product has to be an instance of class Product.")
            koszyk.add_product(element, 1)

        return koszyk.generate_report()

p1 = Product(1, 'Woda', 10.99)
p2 = Product(2, 'Chleb', 4.99)
backset = Basket.with_products([p1, p2])

