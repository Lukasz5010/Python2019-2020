class Zbiornik:
    def __init__(self):
        self.ile_wody=0
        self.temperatura=0

    def odlej(self,ile):
        if self.ile_wody<ile:
            raise ValueError('Wody musi byc wiecej lub tyle samo niz chcesz odlac')
        else:
            self.ile_wody-=ile

    def dolej(self, ile, tmp):
        if self.ile_wody==0:
            self.temperatura=tmp
            self.ile_wody+=ile
        else:
            self.temperatura = ((tmp * ile) + (self.temperatura * self.ile_wody)) / (ile + self.ile_wody)
            self.ile_wody+=ile

    def __str__(self):
        return f'Zbiornik z {self.ile_wody} litrami wody'

a1=Zbiornik()
a1.dolej(5,20)
print(a1.__str__())
a1.dolej(10,40)
print(a1.__str__())