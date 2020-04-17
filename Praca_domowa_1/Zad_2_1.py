#Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
# Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
# Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo,
# aż użytkownik poda prawidłowy wynik.

import random

x = random.randint(0,99)
y = random.randint(0,99)
wynik_uzytkownika = None

wynik = x + y

while wynik != wynik_uzytkownika:
    wynik_uzytkownika = int(input(f"{x} + {y} = "))

print(f"Gratulacje! Prawidłowo obliczyłeś wynik!")