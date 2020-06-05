"""Zaimplementuj iterator zwracający jedynie samogłoski z zadanego ciągu znaków:

Przykładowe użycie:
for char in Vowels('ala ma kota a kot ma ale'):
"""


class Vowels:
    def __init__(self, char: str):
        self.char = char

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        wynik = ""
        if self.number >= len(self.char):
            raise StopIteration

        while True:
            tmp = self.char[self.number]
            if tmp in ["a", "e", "i", "o", "u", "y"]:
                wynik += tmp
                self.number += 1
                return wynik
            else:
                self.number += 1

for char in Vowels("ala ma kota a kot ma ale"):
    print(char)

print(tuple(Vowels("ala ma kota a kot ma ale")))