min=None
max=None
suma=0
srednia=0
ile_liczb=0


while True:
    znak = input("Wpisz slowo \"KONIEC\" jezeli chcesz skonczyc a inny dowolny znak jezeli nie: ")
    if znak.upper() == 'KONIEC':
        break
    liczba = int(input("Wczytaj liczbe: "))
    ile_liczb=ile_liczb+1
    if min == None or liczba < min:
        min = liczba
    if max == None or liczba > max:
        max = liczba
    suma+=liczba

srednia=suma/ile_liczb
print(f"Liczba wczytanych liczb wynosi {ile_liczb} ")
print(f"Suma wszystkich liczb wynosi: {suma}")
print(f"Srednia wczytanych liczb wynosi: {srednia:.2f}")
print(f"Najwieksza liczba wynosi: {max}")
print(f"Najmniejsza liczba wynosi {min}")