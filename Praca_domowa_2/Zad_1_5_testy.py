import pytest

def bmi(waga: float, wzrost: float) -> float:
    """
    oblicza współczynnik BMI dla podanych dwóch parametrów
    :param waga:waga w kg
    :param wzrost: wzrost w m
    :return:współczynnik BMI
    """

    for liczba in waga, wzrost:
        if type(liczba) != float and type(liczba) != int:
            raise TypeError("W argumentach nie podałeś liczby.")
        elif liczba < 0:
            raise ValueError("W argumentach podałeś ujemną liczbę.")

    wynik = round(waga / wzrost ** 2, 2)

    return wynik

def test_zly_argument():
    with pytest.raises(TypeError):
        bmi("a", 1)


def test_ujemny_argument():
    with pytest.raises(ValueError):
        bmi(-10, 5)


def test_rozne_wartosci():
    przyklady = [(55, 1.66, 19.96), (15, 1, 15.0)]

    for waga, wzrost, wsk_bmi in przyklady:
        assert bmi(waga, wzrost) == wsk_bmi
