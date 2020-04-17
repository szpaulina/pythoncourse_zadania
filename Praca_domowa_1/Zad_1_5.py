# Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?),
# a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
# Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
# Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to: import math x = math.sqrt(10)

import math

a = int(input("Podaj pierwszą liczbę (cm): "))
b = int(input("Podaj drugą liczbę (cm): "))
c = int(input("Podaj trzecią liczbę (cm): "))

p = (a + b + c)/2

if (c >= a and c >= b and a + b > c) or (b >= a and b >= c and a + c > b) or (a >= b and a >= c and b + c > a):
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Pole trójkąta wynosi {pole:.2f} cm^2.")
else:
    print(f"Niestety, z podanych liczb nie da się zbudować trójkąta.")
