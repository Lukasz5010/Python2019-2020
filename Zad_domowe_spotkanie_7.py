lista=list()
n = int(input("Podaj dlugosc listy: "))

def Wczytywanie ():
    for i in range(0,n):
        lista.append(int(input("Podaj liczbe: ")))

def ProsteWybieranie (n):

    for i in range(0,n-1):
        k=i
        min=lista[i]
        for j in range(i+1,n):
            if lista[j]<min:
                min=lista[j]
                k=j
        lista[k]=lista[i]
        lista[i]=min



Wczytywanie()
ProsteWybieranie(n)
print(l