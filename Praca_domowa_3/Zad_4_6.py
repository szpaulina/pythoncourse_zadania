class PlanszaXO:
    def __init__(self, rozmiar_x=3, rozmiar_y=3):
        self.rozmiar_x = rozmiar_x
        self.rozmiar_y = rozmiar_y
        self.kolej = 1
        self.wynik = 0
        self.list = [" ", " ", " ",
                     " ", " ", " ",
                     " ", " ", " "]

    def dodaj_element(self, x: int, y: int, rodzaj_elementu):

        if not (1 <= x <= 3 and 1 <= y <= 3 and self.wynik == 0 and ((rodzaj_elementu == "x" and self.kolej % 2 == 1) or (rodzaj_elementu == "o" and self.kolej % 2 == 0))):
            return False
        else:
            indeks = (y-1)*3 + (x-1)
            if self.list[indeks] != " ":
                return False
            else:
                self.list[indeks] = rodzaj_elementu
                self.kolej += 1

    def czyj_ruch(self):
        if self.kolej % 2 == 0:
            return f'Kolej "o"'
        else:
            return f'Kolej "x"'

    def __str__(self):
        return self.printuj()

    def printuj(self):
        return f"{self.list[6]} | {self.list[7]} | {self.list[8]}\n" \
               f"- + - + - \n" \
               f"{self.list[3]} | {self.list[4]} | {self.list[5]}\n" \
               f"- + - + - \n" \
               f"{self.list[0]} | {self.list[1]} | {self.list[2]}"

    def stan_gry(self):
        if self.kolej <= 9:
            if (self.list[6] == self.list[4] == self.list[2] != " ") or (self.list[0] == self.list[4] == self.list[8] != " "):
                self.wynik = 1
                return f"Wygrana {self.list[4]}."
            elif self.list[6] == self.list[3] == self.list[0] != " ":
                self.wynik = 1
                return f"Wygrana {self.list[3]}."
            elif self.list[7] == self.list[4] == self.list[1] != " ":
                self.wynik = 1
                return f"Wygrana {self.list[4]}."
            elif self.list[8] == self.list[5] == self.list[2] != " ":
                self.wynik = 1
                return f"Wygrana {self.list[5]}."
            elif self.list[6] == self.list[7] == self.list[8] != " ":
                self.wynik = 1
                return f"Wygrana {self.list[7]}."
            elif self.list[3] == self.list[4] == self.list[5] != " ":
                self.wynik = 1
                return f"Wygrana {self.list[4]}."
            elif self.list[0] == self.list[1] == self.list[2] != " ":
                self.wynik = 1
                return f"Wygrana {self.list[1]}."
            else:
                return f"Gra w trakcie."
        else:
            self.wynik = 1
            return f"Gra zakończona. Nikt nie wygrał."

z = PlanszaXO()
z.dodaj_element(1, 1, "x")
z.dodaj_element(1, 2, "o")
print(z.stan_gry())
z.dodaj_element(2, 2, "x")
print(z.stan_gry())
z.dodaj_element(3, 3, "o")
z.dodaj_element(3, 1, "x")
print(z)
print(z.stan_gry())
z.dodaj_element(2, 3, "o")
print(z)
print(z.stan_gry())
print(z.czyj_ruch())
z.dodaj_element(1, 3, "x")
print(z)
print(z.stan_gry())
z.dodaj_element(2, 1, "o")
print(z)
print(z.stan_gry())
z.dodaj_element(3, 2, "x")
print(z)
print(z.stan_gry())
z.dodaj_element(3, 2, "x")