#Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
# Np. dla parametru 3 powinno się wypisać:
#
#     *
#   * * *
# * * * * *

wysokosc_choinki = int(input("Podaj wysokość choinki: "))
znak = input("Podaj, z czego ma być zbudowana choinka: ")

for i in range(1,wysokosc_choinki):
    print(" "*(wysokosc_choinki-i) + znak*(2*i-1), end="\n")
    i += 1