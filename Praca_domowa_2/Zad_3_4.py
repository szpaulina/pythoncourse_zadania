def roznica_min_max(lista: list) -> float:
    """
    Funkcja zwraca maksymalną liczbę z listy
    :param lista: lista liczb
    :return: maksymalna liczba z listy
    """
    if not isinstance(lista, list):
        raise TypeError

    znalezione_maksimum = None
    znalezione_minimum = None

    if len(lista) == 0:
        return 0
    else:
        for element in lista:
            if znalezione_maksimum is None or znalezione_maksimum < element:
                znalezione_maksimum = element
            if znalezione_minimum is None or znalezione_minimum > element:
                znalezione_minimum = element

    return znalezione_maksimum - znalezione_minimum
