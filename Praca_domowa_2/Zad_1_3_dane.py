from Praca_domowa_2.Zad_1_3_testy import srednia

liczba_1 = input(f"Podaj liczbę 1.: ")
liczba_2 = input(f"Podaj liczbę 2.: ")

try:
    wynik = srednia(float(liczba_1), float(liczba_2))
    print(f"Średnia liczb {liczba_1} i {liczba_2} równa jest {wynik}.")

except ValueError:
    print("Coś poszło nie tak. Czy na pewno wpisałeś liczby?")
