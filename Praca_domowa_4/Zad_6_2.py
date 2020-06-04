"""Plik z utworem "Pan Tadeusz" do pobrania: http://pgradzinski.students.alx.pl/kpython/pan-tadeusz.txt

Niech program dla podanej nazwy pliku tekstowego i dla podanego słowa policzy ile razy to słowo występuje w pliku (np. Tadeusz w pliku `pan-tadeusz.txt`).
"""
import sys

try:
    file_name = sys.argv[1]

    slowo = str(input(f"Podaj slowo, które mam znaleźć w pliku: {file_name}: "))

    with open(file_name, "r", encoding="utf-8") as file:

        data = file.read()
        wystapienia = 0

        for line in data.split("\n"):
            for word in line.split(" "):
                word = word.replace(".", "")
                word = word.replace(",", "")
                word = word.replace(":", "")
                word = word.replace(";", "")
                word = word.replace("!", "")
                word = word.replace("?", "")
                if word == slowo:
                    wystapienia += 1
        print(f"Słowo {slowo} w pliku '{file_name}' występuje: {wystapienia} razy.")

except FileNotFoundError:
    print(f'Nie znaleziono pliku {file_name}')
    exit(1)

except IndexError:
    print(f'usage: python zad_6_2.py file.txt')
    exit(1)