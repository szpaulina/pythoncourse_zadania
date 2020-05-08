
def suma(lista: list) -> float:
    """
    Funkcja zwraca sumę liczb z listy
    :param lista: lista liczb
    :return: suma liczb z listy
    """
    if not isinstance(lista, list):
        raise TypeError

    wynik = 0

    for element in lista:
            wynik += element

    return wynik