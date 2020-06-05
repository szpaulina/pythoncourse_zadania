"""
Napisz program wczytujący plik z logami aktywności użytkowników w systemie.
Na podstawie wczytanych danych wyświetl informację o sumarycznym czasie
przebywania każdego użytkownika w systemie.

$ python read_logs.py logs_simple.txt
Czas przebywania w systemie:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s
"""
from collections import defaultdict
import csv
import sys

try:
    file_name = sys.argv[1]

    with open(file_name, "r", encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")

        klucze = []
        wartosci = []
        slownik = defaultdict(int)

        for row in csvreader:
            klucze.append(row[0])
            wartosci.append(int(row[1]))

        for indeks, element in enumerate(klucze):
            slownik[element] += wartosci[indeks]
        for uzytkownik, czas in slownik.items():
            print(f"- {uzytkownik}: {czas} s")

except FileNotFoundError:
    print(f'Nie znaleziono pliku {file_name}')
    exit(1)

except IndexError:
    print(f'usage: python Zad_7_3.py file.txt')
    exit(1)
