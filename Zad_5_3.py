import csv
import collections


narodowosci=list()
licznik=collections.defaultdict(int)
with open('zawodnicy.csv', 'r',encoding='utf-8') as pliczek:
    pliczek.seek(0)
    data = pliczek.readlines()
    for line_number, line in enumerate(data, start=1):
        lista = line.split(';')
        if narodowosci == list() or not lista[2] in narodowosci:
            narodowosci.append(lista[2])
        licznik[lista[2]] += 1
    for key, value in licznik.items():
        print(f'{key} - {value}')

