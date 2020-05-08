
from Praca_domowa_2.Zad_1_1_testy import stopy_na_metry

stopy = float(input(f"Podaj liczbę stóp: "))

try:
    wynik = stopy_na_metry(stopy)
    print(f"{stopy} stopy są równe {wynik} metrom.")

except ValueError:
    print(f"Podałeś ujemną liczbę stóp!")