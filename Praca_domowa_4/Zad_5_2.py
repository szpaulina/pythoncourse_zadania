"""Zaimplementuj generator zwracający jedynie samogłoski z zadanego ciągu znaków:

Przykładowe użycie:
for char in vowels('ala ma kota a kot ma ale'):
    ..."""


def vowels(char: str):
    for znak in char:
        if znak in ["a", "e", "i", "o", "u", "y"]:
            yield znak

for char in vowels("ala ma kota a kot ma ale"):
    print(char)

print(tuple(vowels("ala ma kota a kot ma ale")))