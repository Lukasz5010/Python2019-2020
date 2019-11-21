from math import sqrt

def stopy_na_metry(a: float) -> float:
    """
    Funkcja licząca liczbe stop na metry
    :param a: float
    :return: float
    """
    return a*0.25

def max(a: float,b: float) -> float:
    """
    Wybiera maksimum z dwoch liczb
    :param a: float
    :param b: float
    :return: float
    """
    return max(a,b)

def srednia(a: float, b: float) -> float:
    """
    Funkcja oblicza srednia dwoch liczb
    :param a: flaot
    :param b: float
    :return: float
    """
    return (a+b)/2

def pole_kola(r: float) -> float:
    """
    Funkcja liczy pole kola
    :param r: flaot
    :return: float
    """
    return Math.PI*r*r

def bmi(wzrost: float, waga: float) -> float:
    """
    Funkcja obliczba wskaznik BMI
    :param wzrost: float
    :param waga: float
    :return: float
    """
    return waga/(wzrost ** 2)

def pole_trojkata(a: float, b: float, c: float) -> float:
    """
    Funkcja liczby pole trojkata
    :param a: float
    :param b: float
    :param c: float
    :return: float
    """
    if a+b<=c or a+c<=b or b+c<=a:
        return None
    else:
        return sqrt((a+b+c)*(a+b-c)*(b+c-a)*(a+c-b))/4

def kilometry_na_mile(a: float) -> float:
    """
    Funkcja przelicza kilometry na mile
    :param a: float
    :return: float
    """
    return 0.621371192*a

def mile_na_kilometry(a: float) -> float:
    """
    Funkcja zamienia mile na kilometry
    :param a: float
    :return: float
    """
    return 1.609344*a


def test_stopy_na_metry():
    liczba=12
    wynik=stopy_na_metry(liczba)
    assert wynik == 3

def test_max():
    liczba_1=12
    liczba_2=-1
    wynik=max(liczba_1,liczba_2)
    assert wynik == 12

def test_srednia():
    liczba_1=12
    liczba_2=14
    wynik=test_srednia(liczba_1, liczba_2)
    assert wynik == 13

def test_pole_kola():
    liczba=4
    wynik=test_pole_kola(liczba)
    assert wynik == 16*Math.PI

def test_bmi():
    liczba_1=170
    liczba_2=55
    wynik=bmi(liczba_1, liczba_2)
    assert wynik == liczba2/(liczba1 ** 2)

def test_pole_trojkata():
    liczba_1=4
    liczba_2=4
    liczba_3=4
    wynik=test_pole_trojkata(liczba_1, liczba_2, liczba_3)
    assert wynik == sqrt((liczba_1+liczba_2+liczba_3)*(liczba_1+liczba_2-liczba_3)*(liczba_1+liczba_3-liczba_2)*(liczba_2+liczba_3-liczba_1))/4

def test_kilometry_na_mile():
    liczba=1
    wynik=kilometry_na_mile(liczba)
    assert wynik == 0.621371192

def test_mile_na_kilometry():
    liczba=1
    wynik=mile_na_kilometry(liczba)
    assert wynik == 1.609344

mile_na_kilometry(10)
test_mile_na_kilometry()