# Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena. Wyświetl odpowiedni komunikat.
# Przykład:
# Co chcesz kupić? - ziemniaki
# Podaj cenę towaru - 5
# Podaj ilość towaru - 10
# Za ziemniaki, który chcesz kupić, zapłacisz 50 zł

produkt = input("Co chcesz kupić? ")
cena = input("Podaj cenę towaru: ")
ilosc = input("Podaj ilość towaru: ")

wynik = float(cena) * float(ilosc)

print(f"Za {produkt}, który chcesz kupić, zapłacisz: {wynik:.2f} PLN.")