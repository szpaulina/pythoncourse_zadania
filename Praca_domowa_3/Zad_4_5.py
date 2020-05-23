class Zolw:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.kurs = 0
        self.obroty = 0

    def obroc_sie(self, obrot: int):
        if not obrot % 90 == 0:
            raise ValueError("Obrót powinien być wielokrotnością 90 stopni.")

        self.obroty += obrot

        if self.obroty % 360 == 0:
            self.kurs = 0
        elif self.obroty % 360 == 90:
            self.kurs = 1
        elif self.obroty % 360 == 180:
            self.kurs = 2
        else:
            self.kurs = 3

    def idz(self, ruch: int):
        if self.kurs == 0:
            self.y -= ruch
        elif self.kurs == 1:
            self.x += ruch
        elif self.kurs == 2:
            self.y += ruch
        else:
            self.x -= ruch

    def opis(self):
        return f"x = {self.x}, y = {self.y}."

    def __str__(self):
        return self.opis()

z = Zolw(100, 100)
z.idz(50)
print(z)
z.obroc_sie(90)
z.idz(50)
print(z)
z.obroc_sie(90)
z.idz(50)
print(z)
z.obroc_sie(90)
z.idz(50)
print(z)