
def crazy_case(funkcja_do_udekorowania):
    def opakowywacz(*args, **kwargs):
        wynik=funkcja_do_udekorowania()
        napis=''
        for i in range(0,len(wynik)):
            if i%2==1:
                napis+=wynik[i].upper()
            else:
                napis+=wynik[i].lower()
        return napis
    return opakowywacz



@crazy_case
def powiedz_ala():
	return 'Ala ma kota'


print(powiedz_ala()) # aLa mA KoTa