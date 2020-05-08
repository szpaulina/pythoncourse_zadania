1#Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
# oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).

wzrost = float(input(f"Podaj wzrost w cm: "))
masa = float(input(f"Podaj masę w kg: "))

bmi = masa/wzrost**2*100**2

print(f"Twój współczynnik BMI wynosi: {bmi:.2f}.")

if bmi < 16:
    print(f"Jesteś wygłodzony. Natychmmiast zacznij jeść!")
elif 16 <= bmi < 17:
    print(f"Jesteś wychudzony. Zacznij jeść!")
elif 17 <= bmi < 18.5:
    print(f"Masz niedowagę. Spróbuj jeść więcej.")
elif 18.5 <= bmi < 25:
    print(f"Twoja waga jest odpowiednia. Gratulacje!")
elif 25 <= bmi < 30:
    print(f"Masz nadwagę. Spróbuj ograniczyć ilość i kaloryczność spożywanych posiłków, zadbaj o regularny ruch.")
elif 30 <= bmi < 35:
    print(f"Masz I stopień otyłości. Weź się za siebie! Skontaktuj się z dietetykiem, mniej jedz i zacznij ćwiczyć!")
elif 35 <= bmi < 40:
    print(f"Masz II stopień otyłości. Natychmiast weź się za siebie, skontaktuj się z lekarzem, to już ostatni moment na uratowanie Twojego zdrowia!")
else:
    print(f"Twoje BMI wskazuje na otyłość olbrzymią. Natychmiast weź się za siebie, pomyśl o operacji zmniejszenia żołądka!")