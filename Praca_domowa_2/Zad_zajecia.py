import pytest

def srednia(*args):

    if len(args) == 0:
        return None

    for liczba in args:
        if type(liczba) != int and type(liczba) != float:
            raise TypeError("Wśród argumentów jest przynajmniej jeden, który nie jest liczbą.")

    return sum(args) / len(args)

def test_pusty():
    assert srednia() is None

def test_kilka_argumentow():
    assert srednia(10, 20, 30) == 20
    assert srednia(1, 2, 3) == 2

def test_zle_argumenty():
    with pytest.raises(TypeError):
        srednia("a", 1, 2)