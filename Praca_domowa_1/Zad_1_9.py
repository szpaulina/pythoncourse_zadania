#Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
#dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz", end="\n")
    elif i % 3 == 0:
        print(i, "Fizz", end="\n")
    elif i % 5 == 0:
        print(i, "Buzz", end="\n")
    else:
        print(i, end="\n")
