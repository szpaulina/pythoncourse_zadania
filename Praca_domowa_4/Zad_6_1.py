"""Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:

1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)). Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać, być może w innej kolejności:
```
AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
```
4. jak wyżej, ale liczy jeszcze dla każdego kraju średni wzrost zawodników."""

import csv
from collections import defaultdict

with open("zawodnicy.csv", "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")

    imie_nazwisko = []
    wzrosty = []
    wagi = []
    kraj = []

    for row in csvreader:
        imie_nazwisko.append(row[0]+" "+row[1])
        wzrosty.append(row[4])
        wagi.append(row[5])
        kraj.append(row[2])

def wypisywacz():
    indeks_max = wzrosty.index(max(wzrosty))
    indeks_min = wzrosty.index(min(wzrosty))
    indeks_najciezszy = wagi.index(max(wagi))
    indeks_najlzejszy = wagi.index(min(wagi))

    return f"Najwyższy: {imie_nazwisko[indeks_max]}, {wzrosty[indeks_max]} cm.\n"\
           f"Najniższy: {imie_nazwisko[indeks_min]}, {wzrosty[indeks_min]} cm.\n"\
           f"Najcięższy: {imie_nazwisko[indeks_najciezszy]}, {wagi[indeks_najciezszy]} kg.\n"\
           f"Najlżejszy: {imie_nazwisko[indeks_najlzejszy]}, {wagi[indeks_najlzejszy]} kg."

def suma_kraj(nazwa_kraju="POL"):
    suma = 0.0
    if nazwa_kraju in kraj:
        for indeks, element in enumerate(kraj):
            if element == nazwa_kraju:
                suma += float(wagi[indeks])
        return f"Suma wag zawodników z kraju: {nazwa_kraju} to: {suma} kg."
    else:
        raise ValueError

def liczba_zawodników_kraj():
    slownik = defaultdict(int)

    for nazwa_kraju in kraj:
            slownik[nazwa_kraju] += 1
    for klucz, wartosc in slownik.items():
        print(f"{klucz} - {wartosc}")
    return ""
    #return slownik.items()

def srednia_zawodników_kraj():
    slownik = defaultdict(float)
    wystepowanie = defaultdict(int)

    for indeks, element in enumerate(kraj):
            slownik[element] += float(wzrosty[indeks])
            wystepowanie[element] += 1
    for klucz, wartosc in slownik.items():
        srednia = wartosc/wystepowanie[klucz]
        print(f"{klucz} - {srednia:.2f}")
    return ""

print(wypisywacz())

nazwa_kraj = input("Podaj kraj: ")
try:
    print(suma_kraj(nazwa_kraj.upper()))
except ValueError:
    print("No data to show.")
print()
print(liczba_zawodników_kraj())
print(srednia_zawodników_kraj())

