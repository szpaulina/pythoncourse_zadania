def pierwsza_wieksza(lista: list, liczba_x: float) -> float:
    """
    Funkcja wypisuje pierwszą liczbę z listy, która jest większa od x, jeśli takiej nie ma, zwraca None
    :param lista: lista liczb
    :param liczba_x: liczba, od której pierwszą większą liczbę funkcja ma wypisać
    :return: pierwsza liczba większa od x lub None
    """
    if not (isinstance(lista, list) and (type(liczba_x) == float or type(liczba_x) == int)):
        raise TypeError

    for element in lista:
        if element > liczba_x:
            wynik = element
            break
        else:
            wynik = None

    return wynik
