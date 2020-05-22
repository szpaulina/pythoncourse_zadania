class Ogloszenie:
    def __init__(self, tytul, przedmiot: str, opis_przedmiotu: str, stan_przedmiotu: str, cena: float, dane_kontaktowe: str):
        self.tytul = tytul
        self.przedmiot = przedmiot
        self.opis_przedmiotu = opis_przedmiotu
        self.stan_przedmiotu = stan_przedmiotu
        self.cena = cena
        self.dane_kontaktowe = dane_kontaktowe

    def prepare_advertisement(self) -> str:
        return f'{self.tytul}! \n' \
               f'Co: {self.przedmiot}, {self.opis_przedmiotu} \n' \
               f'Stan: {self.stan_przedmiotu}, \n' \
               f'Cena: {self.cena} PLN, \n' \
               f'Dane do kontaktu: {self.dane_kontaktowe}.'

    def __str__(self):
        return self.prepare_advertisement()

    def print_advertisement(self) -> str:
        print(self.prepare_advertisement())

p1 = Ogloszenie("Sprzedam", "bluzka", "czerwona w kropki","nienoszona", 20.5, "tel: 3334444555")
p1.print_advertisement()
