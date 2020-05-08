def znajdz_wspolny(lista1: list, lista2: list) -> float:
    """
    Funkcja wypisuje pierwszą liczbę z listy, która jest podzielna przez x
    :param lista: lista liczb
    :param liczba_x: liczba, przez którą pierwszą podzielną liczbę funkcja ma wypisać
    :return: pierwsza liczba podzieln przez x
    """
    if not isinstance(lista1, list):
        raise TypeError

    if not isinstance(lista2, list):
        raise TypeError

    wynik = None

    for element1 in lista1:
        for element2 in lista2:
            if element1 == element2:
                wynik = element1

    return wynik