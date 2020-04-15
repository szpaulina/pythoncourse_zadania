#Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.).
# Ma też podać, ile dni będzie trwała naprawa.

#Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
#Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni."""

dzien_tyg = int(input(f"Podaj dzień tygodnia, w którym oddałeś buty (1 - poniedziałek, 2 - wtorek itp.): "))
czas = int(input(f"Podaj, ile dni będzie trwała naprawa: "))

dzien_odbioru = (dzien_tyg + czas ) % 7

if dzien_odbioru == 1:
    print(f"Odbierzesz buty w poniedziałek.")
elif dzien_odbioru == 2:
    print(f"Odbierzesz buty we wtorek.")
elif dzien_odbioru == 3:
    print(f"Odbierzesz buty w środę.")
elif dzien_odbioru == 4:
    print(f"Odbierzesz buty w czwartek.")
elif dzien_odbioru == 5:
    print(f"Odbierzesz buty w piątek.")
elif dzien_odbioru == 6:
    print(f"Odbierzesz buty w sobotę.")
else:
    print(f"Odbierzesz buty w niedzielę.")


