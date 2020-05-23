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
        if (self.list[6] == self.list[4] == self.list[2]) or (self.list[0] == self.list[4] == self.list[8]) or (self.list[7] == self.list[4] == self.list[1]) or (self.list[3] == self.list[4] == self.list[5]):
            if self.list[4] == "x" and self.list[4] != " ":
                return f"Wygrana krzyżyków."
            elif self.list[4] == "o" and self.list[4] != " ":
                return f"Wygrana kółek."
            else:
                return f"Gra w trakcie"
        elif (self.list[6] == self.list[3] == self.list[0]) or (self.list[6] == self.list[7] == self.list[8]):
            if self.list[6] == "x" and self.list[6] != " ":
                return f"Wygrana krzyżyków."
            elif self.list[6] == "o" and self.list[6] != " ":
                return f"Wygrana kółek."
            else:
                return f"Gra w trakcie"
        elif (self.list[0] == self.list[1] == self.list[2]) or (self.list[2] == self.list[5] == self.list[8]):
            if self.list[2] == "x" and self.list[2] != " ":
                return f"Wygrana krzyżyków."
            elif self.list[2] == "o" and self.list[2] != " ":
                return f"Wygrana kółek."
            else:
                return f"Gra w trakcie"