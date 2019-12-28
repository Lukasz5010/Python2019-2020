import collections
import operator

liczba_wystapien=collections.defaultdict(int)
lista=list()
suma=0
znaki=0
with open('Pan_Tadeusz.txt', 'r', encoding='utf-8') as file:
    file.seek(0)
    while True:
        linia=file.readline()
        if not linia:
            break
        else:
            lista=linia.split(' ')
            for i in lista:
                if len(i)>=2 :
                    liczba_wystapien[i]+=1
    sorted_key = sorted(liczba_wystapien.items(), key=operator.itemgetter(0))
    sorted_dict = collections.OrderedDict(sorted_key)
    for key, value in sorted_dict.items():
        print(f'{key} - {value}')
        suma+=sorted_dict[key]
    file.seek(0)
    while True:
        linia = file.readline()
        if not linia:
            break
        else:
            znaki+=len(linia)

    print(f'Liczba slow wynosi {suma} a liczna znakow wynosi {znaki}')



