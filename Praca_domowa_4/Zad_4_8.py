"""Zaimplementuj metodę statyczną tworzącą koszyk na podstawie listy podanych produktów.
Każdy z nich powinien zostać dodany do koszyka tylko raz.

Przykład użycia:
backset = Basket.with_products([prod_1, prod_2])"""


class Basket:

    @staticmethod
    def with_products(lista: list):
        if not isinstance(lista, list):
            raise TypeError("Lista has to be an instance of list.")

        koszyk = []

        for element in lista:
            if element not in koszyk:
                koszyk.append(element)
            else:
                continue

        return koszyk

basket = Basket.with_products(["woda", "chleb", "chleb", "lizak"])
print(basket)