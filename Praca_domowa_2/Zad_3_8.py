def ile_wiekszych(lista: list, liczba_x: float) -> float:
    """
    Funkcja wypisuje liczbę elementów, które są większe od x
    :param lista: lista liczb
    :param liczba_x: liczba, od której większe liczby funkcja ma zliczyc
    :return: liczba liczb większych od x
    """
    if not (isinstance(lista, list) and (type(liczba_x) == float or type(liczba_x) == int)):
        raise TypeError

    wynik = 0

    for element in lista:
        if element > liczba_x:
            wynik += 1

    return wynik
