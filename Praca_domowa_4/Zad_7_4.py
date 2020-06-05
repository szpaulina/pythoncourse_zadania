from collections import defaultdict
import csv
import sys

try:
    file_name = sys.argv[1]

    with open(file_name, "r", encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")

        klucze = []
        info = []
        wartosci = []
        slownik = defaultdict(int)

        for row in csvreader:
            klucze.append(row[0])
            info.append(row[1])
            wartosci.append(int(row[2]))

        for indeks, uzytkownik in enumerate(klucze):
            if info[indeks] == "LOGOUT":
                slownik[uzytkownik] += wartosci[indeks]
            elif info[indeks] == "LOGIN":
                slownik[uzytkownik] -= wartosci[indeks]
        for uzytkownik, czas in slownik.items():
            print(f"- {uzytkownik}: {czas} s")

except FileNotFoundError:
    print(f'Nie znaleziono pliku {file_name}')
    exit(1)

except IndexError:
    print(f'usage: python Zad_7_4.py file.txt')
    exit(1)