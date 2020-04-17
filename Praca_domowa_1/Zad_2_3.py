#Napisz program, który odczytuje od użytkownika wiele liczb.
#Program powinien wyliczyć i na końcu wypisać następujące statystyki:
#liczba podanych liczb (ile sztuk),
#suma,
#średnia,
#minimum
#maksimum
#NIE używaj funkcji wbudowanych!

wprowadzone_liczby = 0
suma_liczb = 0
srednia_liczb = 0
minimum_liczb = None
maximum_liczb = None

while True:
    dana = input("Podaj liczbę lub wpisz END: ")

    if dana == "END" or dana =="end":
        break

    if dana.isdecimal() is False:
        print("Niepoprawna liczba")

        continue

    liczba = int(dana)

    wprowadzone_liczby += 1
    suma_liczb += liczba
    srednia_liczb = suma_liczb/wprowadzone_liczby

    if minimum_liczb is None or liczba < minimum_liczb:
        minimum_liczb = liczba
    if maximum_liczb is None or liczba > maximum_liczb:
        maximum_liczb = liczba

if wprowadzone_liczby == 0:
    print("Nie wprowadziłeś nawet jednej poprawnej liczby. Kończę, pozdrawiam.")
else:
    print(f"Wprowadziłeś poprawnych liczb: {wprowadzone_liczby}")
    print(f"Suma: {suma_liczb}")
    print(f"Średnia: {srednia_liczb}")
    print(f"Minimum: {minimum_liczb}")
    print(f"Maksimum: {maximum_liczb}")