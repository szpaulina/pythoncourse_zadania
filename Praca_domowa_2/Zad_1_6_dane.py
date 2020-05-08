from Praca_domowa_2.Zad_1_6_testy import pole_trojkata

bok_a = input(f"Podaj bok a: ")
bok_b = input(f"Podaj bok b: ")
bok_c = input(f"Podaj bok c: ")

try:
    wynik = pole_trojkata(float(bok_a), float(bok_b), float(bok_c))
    print(f"Pole trójkąta o bokach {bok_a}, {bok_b} i {bok_c} to {wynik}.")

except ValueError:
    print(f"Coś poszło nie tak. Z takich boków nie zbuduję trójkąta.")