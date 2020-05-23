from Praca_domowa_3.Zad_4_1 import Ogloszenie


class OgloszenieSamochodowe(Ogloszenie):
    def __init__(self, tytul: str, przedmiot: str, opis_przedmiotu: str, stan_przedmiotu: str, cena: float, dane_kontaktowe: str, model: str, marka: str, rok_produkcji: int, przebieg: int, pojemnosc: int, moc: int, rodzaj_paliwa: str):
        super().__init__(tytul, przedmiot, opis_przedmiotu, stan_przedmiotu, cena, dane_kontaktowe)
        self.model = model
        self.marka = marka
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        self.pojemnosc = pojemnosc
        self.moc = moc
        self.rodzaj_paliwa = rodzaj_paliwa


class OgloszenieMieszkaniowe(Ogloszenie):
    def __init__(self, tytul: str, przedmiot: str, opis_przedmiotu: str, stan_przedmiotu: str, cena: float, dane_kontaktowe: str, miejscowosc: str, metraz: int, liczba_pokoi: int):
        super().__init__(tytul, przedmiot, opis_przedmiotu, stan_przedmiotu, cena, dane_kontaktowe)
        self.miejscowosc = miejscowosc
        self.metraz = metraz
        self.liczba_pokoi = liczba_pokoi


