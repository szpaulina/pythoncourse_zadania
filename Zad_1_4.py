#Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić.
# Zasady są takie:
# - nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# - 200 zł za noc, jeśli nocują jedną noc
# - 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# - 150 zł za noc, jeśli nocują pięć lub więcej nocy
# - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
# Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki,
# czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

wiek = int(input("Podaj proszę swój wiek: "))
liczba_nocy = int(input("Ile nocy spędzisz w hotelu? "))

if wiek < 18:
    wynik = 100*liczba_nocy
else:
    if liczba_nocy < 2:
        wynik = 200*liczba_nocy
    elif 2 <= liczba_nocy < 5:
        wynik = 150*liczba_nocy
    else:
        wynik = 150*liczba_nocy

if wiek >= 65:
   wynik *= 0.9

print(f"Za pobyt zapłacisz: {wynik} PLN.")