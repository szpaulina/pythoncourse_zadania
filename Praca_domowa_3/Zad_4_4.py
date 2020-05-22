class Zbiornik:
    def __init__(self, ilosc_wody=0):
        self.ilosc_wody = ilosc_wody
        self.temp_zbiornika = 0.0

    def dolej(self, ile: float, temperatura: float):
        ilosc_wody_startowa = self.ilosc_wody
        self.ilosc_wody += ile
        self.temp_zbiornika = (ilosc_wody_startowa*self.temp_zbiornika + ile*temperatura)/self.ilosc_wody

    def odlej(self, ile: float):
        if ile > self.ilosc_wody:
            self.ilosc_wody = 0
            self.temp_zbiornika = 0
        else:
            self.ilosc_wody -= ile

    def opis(self):
        return f"Zbiornik z {self.ilosc_wody} litrami wody o temperaturze {self.temp_zbiornika:.1f} st Celsjusza."

    def __str__(self):
        return self.opis()
