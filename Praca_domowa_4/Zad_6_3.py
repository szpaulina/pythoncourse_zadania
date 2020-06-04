"""Podstawowa funkcjonalność:
Napisz program, który czyta plik tekstowy i wylicza oraz wypisuje bez powtórzeń wszystkie słowa występujące w pliku wraz z informacją ile razy dane słowo występuje. Na przykład w ten sposób:

```
Zosia -> 34
Asesor -> 35
dwóch -> 35
Tadeusz -> 107
```

Ewentualne uproszczenie (w razie problemów z wypisywaniem): wypisz tylko jedno najczęściej występujące słowo.

Dalsze rozszerzenia (opcjonalnie):
- posortuj wypisywane słowa
- oprócz liczby poszczególnych słów policz i wypisz także liczbę wszystkich słów, łączną liczbę wszystkich znaków.
"""
import sys
from collections import defaultdict

try:
    file_name = sys.argv[1]

    with open(file_name, "r", encoding="utf-8") as file:

        data = file.read()
        slownik_slowa = defaultdict(int)
        sortowanie = []
        znaki = 0
        wystepowanie = 0

        for line in data.split("\n"):
            for word in line.split(" "):
                word = word.replace(".", "")
                word = word.replace(",", "")
                word = word.replace(":", "")
                word = word.replace(";", "")
                word = word.replace("!", "")
                word = word.replace("?", "")
                word = word.replace("—", "")
                word = word.replace("(", "")
                word = word.replace(")", "")
                word = word.replace("…", "")
                word = word.replace("*", "")
                if word != "":
                    slownik_slowa[word] += 1
                    znaki += len(word)
                    wystepowanie += 1

        for slowo, wystapienia in slownik_slowa.items():
            sortowanie.append(slowo)
        sortowanie.sort()

        for slowo in sortowanie:
            print(f"{slowo} -> {slownik_slowa[slowo]}")

        print(f"Znaków w pliku '{file_name}'(bez spacji i znaków specjalnych): {znaki}")
        print(f"Słów w pliku '{file_name}': {wystepowanie}")

except FileNotFoundError:
    print(f'Nie znaleziono pliku {file_name}')
    exit(1)

except IndexError:
    print(f'usage: python zad_6_3.py file.txt')
    exit(1)