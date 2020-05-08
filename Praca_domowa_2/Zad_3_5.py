def wypisz_wieksze(lista: list, liczba_x: float):
    """
    Funkcja wypisuje wszystkie te liczby z listy, które są większe od x
    :param lista: lista liczb
    :param liczba_x: liczba, od której większe liczby funkcja ma wypisać
    :return: liczby większe od x
    """
    if not isinstance(lista, list):
        raise TypeError

    if not (type(liczba_x) == float or type(liczba_x) == int):
        raise TypeError

    wynik = []

    for element in lista:
        if element > liczba_x:
            wynik.append(str(element))

    return " ".join(wynik)

