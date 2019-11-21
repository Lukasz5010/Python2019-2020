def miesiace(nazwa_miesiaca:str):
    """
    Zwraca liczbe dni jakie ma dany miesiac
    :param nazwa_miesiaca: str
    :return: int
    """
    nazwa_miesiaca = nazwa_miesiaca.lower()
    if nazwa_miesiaca == "styczen":
        return 31
    elif nazwa_miesiaca == "luty":
        ktory_rok = int(input("Ktory rok masz na mysli: "))
        if ktory_rok%4 != 0 or (ktory_rok%400 != 0 and ktory_rok%100 == 0):
            return 28
        else:
            return 29
    elif nazwa_miesiaca == "marzec":
        return 31
    elif nazwa_miesiaca == "kwiecien":
        return 30
    elif nazwa_miesiaca == "maj":
        return 31
    elif nazwa_miesiaca == "czerwiec":
        return 30
    elif nazwa_miesiaca == "lipiec":
        return 31
    elif nazwa_miesiaca == "sierpien":
        return 31
    elif nazwa_miesiaca == "wrzesien":
        return 30
    elif nazwa_miesiaca == "pazdziernik":
        return 31
    elif nazwa_miesiaca == "listopad":
        return 30
    elif nazwa_miesiaca == "grudzien":
        return 31
    else:
        raise ValueError("Nie ma takiego miesiaca")


