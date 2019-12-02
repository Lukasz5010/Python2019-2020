import math
class Zolw:
    def __init__(self, wspolrzedna_x:float, wspolrzedna_y:float):
        self.wspolrzedna_x=wspolrzedna_x
        self.wspolrzedna_y=wspolrzedna_y
        self.kat=0

    def idz(self, o_ile):
        if self.kat == 0:
            self.wspolrzedna_y-=o_ile
        elif self.kat == 180:
            self.wspolrzedna_y+=o_ile
        else:
            self.wspolrzedna_y+=math.sin(self.kat-90)*o_ile
            self.wspolrzedna_x+=math.cos(self.kat-90)*o_ile

    def obroc_sie(self, o_jaki_kat):
        self.kat+=o_jaki_kat
        self.kat=self.kat%360

    def __str__(self):
        return f'x={self.wspolrzedna_x}, y={self.wspolrzedna_y}'

z = Zolw(100, 100)
z.idz(50)
print(z) # ma sie wypisac: x=100, y=50
z.obroc_sie(90)
z.idz(50)
print(z)