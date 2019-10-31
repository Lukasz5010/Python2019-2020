import random
liczba1=random.randint(0,99)
liczba2=random.randint(0,99)
suma_prawidlowa=liczba1+liczba2
suma=int(input(f"Podaj sumę liczb {liczba1} i {liczba2}: "))
if suma!=suma_prawidlowa:
    while suma!=suma_prawidlowa:
        print("Zle policzyles sprobuj ponownie.")
        suma=int(input(f"Podaj sumę liczb {liczba1} i {liczba2}: "))

print("Brawo odgadles liczbe.")
