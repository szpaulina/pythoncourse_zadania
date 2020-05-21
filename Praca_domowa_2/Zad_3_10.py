
def pierwsza_podzielna(lista: list, liczba_x: float) -> float:
    """
    Funkcja wypisuje pierwszą liczbę z listy, która jest podzielna przez x
    :param lista: lista liczb
    :param liczba_x: liczba, przez którą pierwszą podzielną liczbę funkcja ma wypisać
    :return: pierwsza liczba podzieln przez x
    """
    if not (isinstance(lista, list) and (type(liczba_x) == float or type(liczba_x) == int)):
        raise TypeError

    for element in lista:
        if element % liczba_x == 0:
            wynik = element
            break
        else:
            wynik = None

    return wynik
