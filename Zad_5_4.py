import csv
import collections


narodowosci=list()
licznik=collections.defaultdict(int)
wzrost_sredni_narodowosci=collections.defaultdict(int)
with open('zawodnicy.csv', 'r',encoding='utf-8') as pliczek:
    pliczek.seek(0)
    data = pliczek.readlines()
    for line_number, line in enumerate(data, start=1):
        lista = line.split(';')
        if narodowosci==list() or not lista[2] in narodowosci:
            narodowosci.append(lista[2])
        licznik[lista[2]] += 1

    pliczek.seek(0)
    data = pliczek.readlines()  # lista linii, ignoruje ostatnia pusta linie
    for line_number, line in enumerate(data, start=1):
        lista = line.split(';')
        lista[4] = float(lista[4])
        wzrost_sredni_narodowosci[lista[2]]+=lista[4]
    for key, value in licznik.items():
        wzrost_sredni_narodowosci[key]=wzrost_sredni_narodowosci[key]/licznik[key] #nie wiem czy ten zabieg nie jest ryzykowny
    for key, value in wzrost_sredni_narodowosci.items():
        print(f'Sredni wzrost narodowosci {key} to: {value:.2f}')




