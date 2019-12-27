import csv


with open('zawodnicy.csv', 'r', encoding='utf-8') as file:
    max_height=None
    najwyzszy_skoczek = ''
    max_weight=None
    najciezszy_skoczek = ''
    min_height=None
    najnizszy_skoczek= ''
    min_weight=None
    najlzejszy_skoczek = ''
        # podejscie 1
    file.seek(0)
    data = file.readlines()  # lista linii, ignoruje ostatnia pusta linie
    print(data)
    for line_number, line in enumerate(data, start=1):
        lista_podzielona=line.split(';')
        lista_podzielona[4]=int(lista_podzielona[4])
        lista_podzielona[5]=int(lista_podzielona[5])
        if max_height==lista_podzielona[4]:
            najwyzszy_skoczek+=', '
            najwyzszy_skoczek += lista_podzielona[0]
            najwyzszy_skoczek += ' '
            najwyzszy_skoczek += lista_podzielona[1]
        elif max_height==None or max_height<lista_podzielona[4]:
            max_height=lista_podzielona[4]
            najwyzszy_skoczek=lista_podzielona[0]
            najwyzszy_skoczek += ' '
            najwyzszy_skoczek+=lista_podzielona[1]
        if min_height==lista_podzielona[4]:
            najniższy_skoczek+=', '
            najnizszy_skoczek += lista_podzielona[0]
            najnizszy_skoczek += ' '
            najnizszy_skoczek += lista_podzielona[1]
        elif min_height==None or min_height>lista_podzielona[4]:
            min_height=lista_podzielona[4]
            najnizszy_skoczek=lista_podzielona[0]
            najnizszy_skoczek += ' '
            najnizszy_skoczek += lista_podzielona[1]
        if max_weight==lista_podzielona[5]:
            najciezszy_skoczek+=', '
            najciezszy_skoczek += lista_podzielona[0]
            najciezszy_skoczek += ' '
            najciezszy_skoczek += lista_podzielona[1]
        elif max_weight==None or max_weight<lista_podzielona[5]:
            max_weight=lista_podzielona[5]
            najciezszy_skoczek=lista_podzielona[0]
            najciezszy_skoczek += ' '
            najciezszy_skoczek+=lista_podzielona[1]
        if min_weight == lista_podzielona[5]:
            najlzejszy_skoczek+=', '
            najlzejszy_skoczek += lista_podzielona[0]
            najlzejszy_skoczek += ' '
            najlzejszy_skoczek += lista_podzielona[1]
        elif min_weight==None or min_weight>lista_podzielona[5]:
            min_weight=lista_podzielona[5]
            najlzejszy_skoczek=lista_podzielona[0]
            najlzejszy_skoczek += ' '
            najlzejszy_skoczek+=lista_podzielona[1]

    print(f'Najwyzszy skoczek to: {najwyzszy_skoczek}')
    print(f'Najnizszy skoczek to: {najnizszy_skoczek}')
    print(f'Najciezszy skoczek to: {najciezszy_skoczek}')
    print(f'Najlzejszy skoczek to: {najlzejszy_skoczek}')





