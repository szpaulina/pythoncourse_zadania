import pytest

def srednia(*args: float) -> float:
    """
    Funkcja zwraca średnią z dwóch liczb
    :param args: wprowadzone liczby
    :return: średnia z dwóch wprowadzonych liczb
    """

    if len(args) == 0:
        return None

    for liczba in args:
        if type(liczba) != int and type(liczba) != float or len(args) != 2:
            raise TypeError("Wśród argumentów jest przynajmniej jeden, który nie jest liczbą, lub podałeś więcej niż 2 liczby.")

    return sum(args)/len(args)

def test_pusty():
    assert srednia() is None

def test_zly_argument():
    with pytest.raises(TypeError):
        srednia("a", 2)

def test_rozne_wartosci():
    przyklady = [(0, 1, 0.5), (10, 20, 15), (20, -10, 5), (10, -40, -15)]

    for liczba_1, liczba_2, wynik in przyklady:
        assert srednia(liczba_1, liczba_2) == wynik
