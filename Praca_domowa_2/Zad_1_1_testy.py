import pytest

def stopy_na_metry(stopy: float) -> float:
    """
    Funkcja przelicza stopy na metry
    :param stopy: wartość w stopach
    :return: wartość w metrach
    """

    if type(stopy) != int and type(stopy) != float:
        raise TypeError("W argumencie nie podałeś liczby.")
    elif stopy < 0:
        raise ValueError("Podałeś ujemną liczbę stóp.")

    wynik = stopy * 0.4048
    return wynik


def test_zly_argument():
    with pytest.raises(TypeError):
        stopy_na_metry("a")


def test_ujemny_argument():
    with pytest.raises(ValueError):
        stopy_na_metry(-10)


def test_rozne_wartosci():
    przyklady = [(0, 0), (1, 0.3048), (2, 0.6096), (10, 3.048)]

    for stopy, metry in przyklady:
        assert stopy_na_metry(stopy) == metry
