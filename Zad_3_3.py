import pytest

lista=list()



def wczytywanie(lista):
    while True:
        napis = input("Wybierz jedna z opcji, aby kontynuowac: ")
        napis = napis.lower()
        if napis == "koniec":
            break
        elif napis == "start":
            liczba = int(input("Podaj liczbe: "))
            lista.append(liczba)
        else:
            raise ValueError("Podales bledne dane")


def suma(lista):
    suma=0
    for i in range(0, len(lista)):
        suma+=lista[i]
    return suma

def srednia(lista):
    wynik=suma(lista)/len(lista)
    return wynik

def max(lista):
    max=None
    for i in lista:
        if max==None or i>max:
            max=i
    return max

def roznica_min_max(lista):
    min=None
    for i in lista:
        if min==None or i<min:
            min=i
    if lista==list():
        return 0
    return max(lista)-min

def wypisz_wieksze(lista,x):
    pom=list()
    for i in lista:
        if i>x:
            pom.append(i)
    print(f"Liczby wiekszsze od x to: {pom}")

def pierwsza_wieksza(lista,x):
    for i in lista:
        if i>x:
            return i
    return None

def suma_wiekszych(lista,x):
    suma=0
    pom = list()
    for i in lista:
        if i > x:
            pom.append(i)
    for i in pom:
        suma+=i
    return suma

def ile_wiekszych(lista,x):
    pom = list()
    for i in lista:
        if i > x:
            pom.append(i)
    return len(pom)

def wypisz_podzielne(tab,x):
    podzielne=list()
    for i in tab:
        if i%x==0:
            podzielne.append(i)
    print(f"Liczby podzielne przez {x} to {podzielne}")

def pierwsza_podzielna(tab,x):
    for i in tab:
        if i%x==0:
            return i
    return None


def znajdz_wspolny(liczby1, liczby2):
    for i in liczby1:
        for j in liczby2:
            if i==j:
                return i
    return None


wczytywanie(lista)
print(suma([2,3]))
print(srednia([2,3,4]))
print(max([2,3,4]))
print(roznica_min_max([2,3,4]))
wypisz_wieksze([2,3,4],3)
print(pierwsza_wieksza([4,3,2],3))
print(suma_wiekszych([4,3,2],2))
print(ile_wiekszych([5,4,3,2],3))
wypisz_podzielne([6,5,4,3,2],2)
print(pierwsza_podzielna([6,5,4,3,2],2))
print(znajdz_wspolny([1,2,3],[2,3,4]))