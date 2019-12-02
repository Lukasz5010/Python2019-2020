class Samochod:
    def __init__(self, marka:str, przebieg:int, rok_produkcji:int, spalanie_na_sto_km:float, cena:float):
        self.marka=marka
        self.przebieg=przebieg
        self.rok_produkcji=rok_produkcji
        self.spalanie_na_sto_km=spalanie_na_sto_km
        self.cena=cena
        self.lista=list()



    def dodawanie_do_listy(self):
        self.lista.append(self.marka)
        self.lista.append(self.przebieg)
        self.lista.append(self.rok_produkcji)
        self.lista.append(self.spalanie_na_sto_km)
        self.lista.append(self.cena)
        return self.lista


    def dodanie_do_listy_ogolnej(self):
        lista_ogolna=list()
        lista_ogolna+=self.lista
        print(lista_ogolna)

    def print_listy(self):
        return f"Lista samochodow wraz z atrybutami wyglada tak: {self}"




s1=Samochod('Opel Astra', 80000, 2015, 5.9, 16500)
s2=Samochod('Opel Astra', 120000, 2013, 5.8, 15500)
s3=Samochod('Audi A4', 90000, 2015, 6.2, 19500)

a=s1.dodawanie_do_listy()
b=s2.dodawanie_do_listy()
c=s3.dodawanie_do_listy()

lista_ogolna=list()
lista_ogolna.append(a)
lista_ogolna.append(b)
lista_ogolna.append(c)
print(lista_ogolna)

przebieg_powyzej_100000=list(filter(lambda i:i[1]>=100000,lista_ogolna))
print(przebieg_powyzej_100000)
ople_astra=list(filter(lambda i:i[0]=='Opel Astra',lista_ogolna))
print(ople_astra)