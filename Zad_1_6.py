# Założenia:
#	- 0-6   - wiek przedszkolny - cena biletu: 0
#	- 7-17  - wiek szkolny      - cena biletu: 2.28
#	- 18-64 - wiek dorosły      - cena biletu: 3.80
#	- +65   - wiek emerytalny   - cena biletu: 1.90
# Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
# Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
# Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.

wiek = int(input("Jaki jest Twój wiek? "))
l_biletow = int(input("Ile biletów chcesz kupic? "))

if 0 <= wiek <= 6:
    print(f"Dzieci do lat 6 nie płacą za bilety! Zapraszamy!")
    exit()
elif 6 < wiek <= 17:
    wynik = 2.28 * l_biletow
elif 17 < wiek <= 64:
    wynik = 3.8 * l_biletow
elif 64 < wiek:
    wynik = 1.9 * l_biletow
else:
    print(f"Wygląda na to, że jeszcze się nie urodziłeś :)")
    exit()

print(f"Za bilety zapłacisz: {wynik:.2f} PLN.")