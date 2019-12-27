import csv

try:
    with open('zawodnicy.csv', 'r', encoding='utf-8') as file:
        waga = 0
        narodowosc=input('Podaj trzyliterowy skrot badanej narodowosci skoczkow, po to aby dowiedziec sie, ile oni waza: ')
        if narodowosc.lower()!='pol' and narodowosc.lower()!='ger' and narodowosc.lower()!='nor' and narodowosc.lower()!='fin' and narodowosc.lower()=='aut'and narodowosc.lower()!='usa':
            raise ValueError
        file.seek(0)
        data = file.readlines()  # lista linii, ignoruje ostatnia pusta linie
        for line_number, line in enumerate(data, start=1):
            lista=line.split(';')
            lista[5] = int(lista[5])
            if narodowosc.lower()==lista[2].lower():
                waga+=lista[5]


    print(f'Zawodnicy tej kadry waza {waga} kg')
except ValueError:
    print('Podano niewlasciwa narodowosc')

