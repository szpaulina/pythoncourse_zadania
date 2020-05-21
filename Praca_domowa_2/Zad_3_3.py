def daj_maks(lista: list) -> float:
    """
    Funkcja zwraca maksymalną liczbę z listy
    :param lista: lista liczb
    :return: maksymalna liczba z listy
    """
    if not isinstance(lista, list):
        raise TypeError

    znalezione_maksimum = None

    for element in lista:
        if znalezione_maksimum is None or znalezione_maksimum < element:
            znalezione_maksimum = element

    return znalezione_maksimum
