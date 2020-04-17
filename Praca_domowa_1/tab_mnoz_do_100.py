
print(" "*5, end="")

for mnozna in range(0,11):
    print(f"{mnozna:<4}", end="")

print("\n")

for mnozna in range(0, 11):
    print(f"{mnozna:<5}", end="")

    for mnoznik in range (0, 11):
        iloczyn = mnozna*mnoznik
        print(f"{iloczyn:<4}", end="")
    print()