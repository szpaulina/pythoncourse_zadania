import pytest

def daj_maksa(*args: float) -> float:
    """
    Funkcja zwraca większą z dwóch liczb
    :param args: wprowadzone liczby
    :return: większa z dwóch wprowadzonych liczb
    """
    if len(args) == 0:
        return None

    wynik = None

    for liczba in args:

        if type(liczba) != int and type(liczba) != float or len(args) != 2:
            raise TypeError("Wśród argumentów jest przynajmniej jeden, który nie jest liczbą, lub podałeś więcej niż 2 liczby.")
        elif liczba == wynik:
            raise ValueError("Podano takie same liczby")

        elif wynik is None or liczba > wynik:
            wynik = liczba

    return wynik

def test_pusty():
    assert daj_maksa() is None

def test_zly_argument():
    with pytest.raises(TypeError):
        daj_maksa("a", 2)

def test_takie_same_liczby():
    with pytest.raises(ValueError):
        daj_maksa(2, 2)

def test_za_duzo_argumentow():
    with pytest.raises(TypeError):
        daj_maksa(2, 2, 4)

def test_rozne_wartosci():
    przyklady = [(0, 1, 1), (1, 2, 2), (2, -10, 2), (10, -40, 10)]

    for liczba_1, liczba_2, wynik in przyklady:
        assert daj_maksa(liczba_1, liczba_2) == wynik
