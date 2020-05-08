import math
import pytest

def pole_trojkata(a: float, b: float, c: float) -> float:
    """
    Funkcja oblicza pole trójkąta o podanych bokach z wzoru Herona
    :param a: bok a
    :param b: bok b
    :param c: bok c
    :return: pole trojkata
    """

    for liczba in a, b, c:
        if type(liczba) != float and type(liczba) != int:
            raise TypeError("Wśród argumentów jest przynajmniej jeden, który nie jest liczbą.")

    p = (a + b + c) / 2

    if (c >= a and c >= b and a + b > c) or (b >= a and b >= c and a + c > b) or (a >= b and a >= c and b + c > a):
        pole = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    else:
        raise ValueError("Z podanych boków nie zbuduje się trójkąta.")

    return pole

def test_zle_argumenty():
    with pytest.raises(TypeError):
        pole_trojkata("a", 2, 3)
    with pytest.raises(ValueError):
        pole_trojkata(1, 1, 3)

def test_rozne_wartosci():
    przyklady = [(1, 1, 1, 0.43), (3, 4, 5, 6.0), (4, 4, 6, 7.94)]

    for a, b, c, pole in przyklady:
        assert pole_trojkata(a, b, c) == pole