import os
from os import *


# . - oznacza aktualny katalog
# .. - oznacza katalog wyżej
zawartosc_katalogu=os.scandir('..')
try:
    for element in zawartosc_katalogu:
        print('|--',element.name)
        if element.is_dir():
            chdir(element)
        pliki = os.scandir('.')
        for plik in pliki:
            print('|  |',plik.name)
except StopIteration:
    print('Iterator sie skonczyl')









