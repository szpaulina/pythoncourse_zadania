import json
import io

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

czynnosc = input(str("Co chcesz zrobić? [d- dodaj, w- wypisz] "))

with io.open("data.json", "r", encoding="utf-8") as plik:
    data = json.load(plik)
    lista_imion = data["imię"]
    lista_nazwisk = data["nazwisko"]
    lista_rok = data["rok urodzenia"]
    lista_pensja = data["pensja"]

if czynnosc == "d":

    with io.open("data.json", "w", encoding="utf-8") as plik:

        imie = input("Imię: ")
        lista_imion.append(imie)
        data["imię"] = lista_imion
        nazwisko = input("Nazwisko: ")
        lista_nazwisk.append(nazwisko)
        data["nazwisko"] = lista_nazwisk
        rok = input("Rok urodzenia: ")
        lista_rok.append(rok)
        data["wiek"] = lista_rok
        pensja = input("Pensja: ")
        lista_pensja.append(pensja)
        data["pensja"] = lista_pensja

        str_ = json.dumps(data,
                        indent = 4, sort_keys= True,
                        separators=(",", ": "), ensure_ascii=False)
        plik.write(to_unicode(str_))

if czynnosc == "w":
    id = int(input("Id: "))-1
    with io.open("data.json", "r", encoding="utf-8") as plik:
        data = json.load(plik)
        print(f'- {id+1} {data["imię"][id]} {data["nazwisko"][id]} - rok {data["rok urodzenia"][id]}, pensja: {data["pensja"][id]} PLN')



