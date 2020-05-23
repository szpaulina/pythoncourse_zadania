class Pociag:
    def __init__(self, predkosc=10, ilosc_paliwa=1000):
        self.predkosc = predkosc
        self.ilosc_paliwa = ilosc_paliwa

    def opis(self) -> str:
        return f'Moja predkosc to: {self.predkosc}, mam jeszcze: {self.ilosc_paliwa:.2f} litrów paliwa.'

    def przyspiesz(self, o_ile: float) -> float:
        stara_predkosc = self.predkosc
        if o_ile / self.predkosc <= 0.75 and self.ilosc_paliwa != 0:
            self.predkosc += o_ile
            self.ilosc_paliwa -= o_ile * stara_predkosc / 100

    def __str__(self):
        return self.opis()

    def drukuj_opis(self):
        print(self.opis())

def test_ciuchci_5km():
    wagon = Pociag()
    wagon.przyspiesz(5)
    assert wagon.opis() == 'Moja predkosc to: 15, mam jeszcze: 999.50 litrów paliwa.'
    wagon.przyspiesz(20)
    assert wagon.opis() == 'Moja predkosc to: 15, mam jeszcze: 999.50 litrów paliwa.'
    wagon.przyspiesz(8)
    assert wagon.opis() == 'Moja predkosc to: 23, mam jeszcze: 998.30 litrów paliwa.'
    wagon.przyspiesz(10)
    assert wagon.opis() == 'Moja predkosc to: 33, mam jeszcze: 996.00 litrów paliwa.'