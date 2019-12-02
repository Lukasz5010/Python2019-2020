class Pociag:
    def __init__(self):
        self.predkosc=10
        self.ilosc_paliwa=1000

    def opis(self):
        return f'Moja predkosc to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrow paliwa.'



    def przyspiesz(self, o_ile_zwiekszyc:int):
        if self.ilosc_paliwa-(o_ile_zwiekszyc)*(self.predkosc/100)<0:
            print('Paliwa jest za malo')
            return
        if (o_ile_zwiekszyc/self.predkosc)<=0.75:
            stara_predkosc = self.predkosc
            nowa_predkosc=stara_predkosc+o_ile_zwiekszyc
            self.ilosc_paliwa-=(nowa_predkosc-stara_predkosc)*(stara_predkosc/100)
            self.predkosc+=o_ile_zwiekszyc
        else:
            print('Nie mozna zwiekszyc o tyle')

    def __str__(self):
        return f'Pociag {self.predkosc} {self.ilosc_paliwa}'

a1=Pociag()
a1.przyspiesz(5)
print(a1.opis())
a1.przyspiesz(20)
print(a1.opis())
a1.przyspiesz(8)
print(a1.opis())
a1.przyspiesz(10)
print(a1.opis())
