def dni_miesiaca(name: str, rok=2020) -> int:
    """
    Funkcja oblicza liczbę dni w danym miesiącu
    :param name: nazwa miesiąca
    :param rok: rok do obliczeń lutego (opcjonalny)
    :return: liczba dni w miesiącu
    """
    miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień',
                'październik', 'listopad', 'grudzień']
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    name = name.lower()

    for element in miesiace:
        if name == element:
            liczba_dni = dni[miesiace.index(name)]
            break
        else:
            liczba_dni = None

    if liczba_dni is None:
        raise ValueError

    if name == "luty":
        if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
            liczba_dni = 29

    return liczba_dni


miesiac = input("Podaj miesiąc: ")
miesiac = miesiac.lower()

try:
    if miesiac == "luty":
        rok = int(input("Podaj rok, dla którego mam podać liczbę dni: "))
        dni = dni_miesiaca(miesiac, rok)
    else:
        dni = dni_miesiaca(miesiac)

    print(f"Miesiąc {miesiac} ma {dni} dni.")

except ValueError:
    print("Czy na pewno dobrze wpisałeś miesiąc lub rok?")
