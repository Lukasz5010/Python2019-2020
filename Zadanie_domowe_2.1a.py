import random
liczba1=random.randint(0,99)
liczba2=random.randint(0,99)
suma_prawidlowa=liczba1+liczba2

while True:
    suma=int(input(f"Podaj sumę liczb {liczba1} i {liczba2}: "))
    if suma != suma_prawidlowa:
        print("Zle policzyles sprobuj ponownie.")
    else:
        print("Brawo odgadles liczbe.")
        break