
class Ogloszenie:
    def __init__(self, auto_model: str, rok_produkcji: int, stan_auta: str, cena: float, dane_kontaktowe: str):
        self.auto_model = auto_model
        self.rok_produkcji = rok_produkcji
        self.stan_auta = stan_auta
        self.cena = cena
        self.dane_kontaktowe = dane_kontaktowe


    def prepare_advertisement(self) -> str:
        return f'Auto: {self.auto_model},\n' \
               f'Rok produkcji: {self.rok_produkcji}\n' \
               f'Stan: {self.stan_auta}, \n' \
               f'Cena: {self.cena} PLN, \n' \
               f'Dane do kontaktu: {self.dane_kontaktowe}.\n'

    def __str__(self):
        return self.prepare_advertisement()

    def print_advertisement(self) -> str:
        print(self.prepare_advertisement())


a1 = Ogloszenie("Opel Astra", 2010, "idealny", 19999, "tel. 333444555")
a2 = Ogloszenie("Seat Ibiza", 1992, "b.dobry", 2499, "tel. 444555666")
a3 = Ogloszenie("Audi A6", 2000, "wyśmienity", 17999, "tel.555666777")

lista = [a1, a2, a3]
lista_cen = [a1.cena, a2.cena, a3.cena]

cena_max = float(input("Podaj cenę maksymalną: "))

lista_wynikowa = list(filter(lambda cena: cena < cena_max, lista_cen))


if lista_wynikowa == []:
    print("Nie mamy tak tanich aut.")
else:
    print("Te ogłoszenia Cię zainteresują: ")
    for element in lista_wynikowa:
        lista[lista_cen.index(element)].print_advertisement()