while True:
    liczba1 = int(input("Podaj pierwsza liczbe: "))
    znak = input("Podaj znak miedzy liczbami: ")
    liczba2 = int(input("Podja druga liczbe: "))
    if znak == '+':
        print(f"Suma dwoch liczb {liczba1} oraz {liczba2} wynosi: {liczba1+liczba2}")
    elif znak == '-':
        print(f"Roznica dwoch liczb {liczba1} oraz {liczba2} wynosi: {liczba1 - liczba2}")
    elif znak == '*':
        print(f"Iloczyn dwoch liczb {liczba1} oraz {liczba2} wynosi: {liczba1 * liczba2}")
    elif znak == '/':
        print(f"Iloraz dwoch liczb {liczba1} oraz {liczba2} wynosi {liczba1 / liczba2}")
    else:
        print("Niepoprawne dane")

    czy_kontynuowac=input("Czy chcesz kontynuowac? Wpisz w konsole jedna z opcji: Kontynuuj/Koniec: ")
    if czy_kontynuowac.upper()=='KONIEC':
        break
