
def wypisz_podzielne(lista: list, liczba_x: float) -> float:
    """
    Funkcja wypisuje te liczby z listy, które są podzielne przez x
    :param lista: lista liczb
    :param liczba_x: liczba, przez którą podzielne liczby funkcja ma wypisać
    :return: liczby podzielne przez x
    """

    if not (isinstance(lista, list) and (type(liczba_x) == float or type(liczba_x) == int)):
        raise TypeError

    wynik = []

    for element in lista:
        if element % liczba_x == 0:
            wynik.append(str(element))

    return " ".join(wynik)

liczby = [10,20,30, 3, 1, 4]
print(wypisz_podzielne(liczby, 2))