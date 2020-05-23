class PlanszaXO:
    def __init__(self, rozmiar_x=3, rozmiar_y=3):
        self.rozmiar_x = rozmiar_x
        self.rozmiar_y = rozmiar_y
        self.kolej = 1
        self.list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def dodaj_element(self, x: int, y: int, rodzaj_elementu):

        if not (1 <= x <= 3 and 1 <= y <= 3 and ((rodzaj_elementu == "x" and self.kolej % 2 == 1) or (rodzaj_elementu == "o" and self.kolej % 2 == 0))):
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
            return 'Kolej "o"'
        else:
            return 'Kolej "x"'

    def __str__(self):
        return self.printuj()

    def printuj(self):
        return f"----- \n" \
               f"{self.list[6]} {self.list[7]} {self.list[8]}\n" \
               f"{self.list[3]} {self.list[4]} {self.list[5]}\n" \
               f"{self.list[0]} {self.list[1]} {self.list[2]}\n" \
               f"----- \n"

    def stan_gry(self):
        if ((self.list[6] == self.list[4] == self.list[2]) or (self.list[0] == self.list[4] == self.list[8]) or (self.list[7] == self.list[4] == self.list[1]) or (self.list[3] == self.list[4] == self.list[5])) and self.list[4] != " ":
            if self.list[4] == "x":
                return f"Wygrana krzyżyków."
            elif self.list[4] == "o":
                return f"Wygrana kółek."
        elif ((self.list[6] == self.list[3] == self.list[0]) or (self.list[6] == self.list[7] == self.list[8])) and self.list[6] != " ":
            if self.list[6] == "x":
                return f"Wygrana krzyżyków."
            elif self.list[6] == "o":
                return f"Wygrana kółek."
        elif ((self.list[0] == self.list[1] == self.list[2]) or (self.list[2] == self.list[5] == self.list[8])) and self.list[2] != " ":
            if self.list[2] == "x":
                return f"Wygrana krzyżyków."
            elif self.list[2] == "o":
                return f"Wygrana kółek."
        else:
            return f"Gra w trakcie."

z = PlanszaXO()
z.dodaj_element(1, 1, "x")
z.dodaj_element(1, 2, "o")
print(z.stan_gry())
z.dodaj_element(2, 1, "x")
print(z.stan_gry())
z.dodaj_element(2, 2, "o")
z.dodaj_element(3, 1, "x")
print(z)
print(z.stan_gry())
z.dodaj_element(3, 2, "o")
print(z)
print(z.stan_gry())