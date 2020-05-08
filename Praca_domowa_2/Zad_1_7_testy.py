import pytest

def km_na_mile(km: float) -> float:
    """
    Funkcja przelicza odległość wyrażoną w kilometrach na mile
    :param km: odległość w km
    :return: odległość w milach
    """
    if type(km) != int and type(km) != float:
        raise TypeError("W argumencie nie podałeś liczby.")
    elif km < 0:
        raise ValueError("Podałeś ujemną liczbę kilometrów.")

    wynik = round(km * 0.621371192, 2)
    return wynik

    return wynik


def test_zly_argument():
    with pytest.raises(TypeError):
        km_na_mile("a")


def test_ujemny_argument():
    with pytest.raises(ValueError):
        km_na_mile(-10)


def test_rozne_wartosci():
    przyklady = [(0, 0), (1, 0.62), (4, 2.49), (20, 12.43)]

    for km, mile in przyklady:
        assert km_na_mile(km) == mile

