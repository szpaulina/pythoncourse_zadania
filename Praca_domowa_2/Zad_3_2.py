def srednia(lista: list) -> float:
    """
    Funkcja zwraca średnią liczb z listy
    :param lista: lista liczb
    :return: średnia liczb z listy
    """
    if not isinstance(lista, list):
        raise TypeError

    wynik = 0

    for element in lista:
            wynik += element

    return wynik/len(lista)
