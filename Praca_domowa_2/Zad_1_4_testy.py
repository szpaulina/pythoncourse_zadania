import pytest
import math

def pole_kola(promien: float) -> float:
    """
    Funkcja oblicza pole koła przy zadanym promieniu
    :param promien: dlugosc promienia
    :return: pole kola
    """

    if type(promien) != int and type(promien) != float:
        raise TypeError("W argumentach nie podałeś liczby.")
    elif promien < 0:
        raise ValueError("Podałeś ujemną liczbę.")

    wynik = round(math.pi*promien**2, 2)

    return wynik

def test_zly_argument():
    with pytest.raises(TypeError):
        pole_kola("a")


def test_ujemny_argument():
    with pytest.raises(ValueError):
        pole_kola(-10)


def test_rozne_wartosci():
    przyklady = [(0, 0), (1, 3.14), (2, 12.57), (10, 314.16)]

    for promien, pole in przyklady:
        assert pole_kola(promien) == pole