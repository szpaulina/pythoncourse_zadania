#Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.

#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.

#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
# ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
# I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.

cena_ziemniakow = float(input("Cena za kg ziemniaków: "))
kg_ziemniakow = float(input("Napisz proszę, ile kg ziemniaków chcesz kupić: "))
cena_bananow = float(input("Cena za kg bananów: "))
kg_bananow = float(input("Napisz proszę, ile kg bananów chcesz kupić: "))

wynik_ziemniaki = cena_ziemniakow*kg_ziemniakow
wynik_banany = cena_bananow*kg_bananow
wynik_total = wynik_ziemniaki + wynik_banany

print()
print(f"Ziemniaki: {kg_ziemniakow:.2f} kg * {cena_ziemniakow:.2f} zł/kg = {wynik_ziemniaki:.2f} zł.")
print(f"Banany: {kg_bananow:.2f} kg * {cena_bananow:.2f} zł/kg = {wynik_banany:.2f} zł.")
print(f"Twoje zakupy wyniosą łącznie: {wynik_total:.2f} zł.")
if wynik_ziemniaki > wynik_banany:
    print(f"Tym razem więcej zapłacisz za ziemniaki.")
elif wynik_ziemniaki < wynik_banany:
    print(f"Tym razem więcej zapłacisz za banany.")
else:
    print(f"Tym razem zapłacisz tyle samo za ziemniaki i banany.")