liczba_linijek=int(input("Podaj dlugosc choinki: "))


for i in range(1, liczba_linijek+1):
    pierwsza_gwiazdka_w_linijce=liczba_linijek-i+1
    ktora_linijka=i
    for pozycja in range(1,2*liczba_linijek):
        if pozycja>=pierwsza_gwiazdka_w_linijce and pozycja<=2*liczba_linijek-pierwsza_gwiazdka_w_linijce:
            print(" * ",end="")
        else:
            print("   ",end="")
        if pozycja>=2*liczba_linijek-1:
            print()

