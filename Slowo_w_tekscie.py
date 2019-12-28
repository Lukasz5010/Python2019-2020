
with open('Pan_Tadeusz.txt','r',encoding='utf-8') as file:
    licznik=0
    slowo=input('Podaj slowo do sprawdzenia ile razy wystepuje ksiazce pt. Pan Tadeusz: ')
    file.seek(0)
    for line in file:
        print(line)
        licznik+=line.count(f' {slowo} ')
    print(f'Slowo {slowo} wystapilo {licznik}')




