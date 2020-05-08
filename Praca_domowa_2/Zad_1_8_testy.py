import pytest

def mile_na_km(mile: float) -> float:
    """
    Funkcja przelicza odległość wyrażoną w milach na kilometry
    :param mile: odległość w milach
    :return: odległość w kilometrach
    """
    if type(mile) != int and type(mile) != float:
        raise TypeError("W argumencie nie podałeś liczby.")
    elif mile < 0:
        raise ValueError("Podałeś ujemną liczbę mil.")

    wynik = round(mile * 1.609344, 2)
    return wynik

    return wynik


def test_zly_argument():
    with pytest.raises(TypeError):
        mile_na_km("a")


def test_ujemny_argument():
    with pytest.raises(ValueError):
        mile_na_km(-10)


def test_rozne_wartosci():
    przyklady = [(0, 0), (1, 1.61), (4, 6.44), (20, 32.19)]

    for mile, km in przyklady:
        assert mile_na_km(mile) == km
