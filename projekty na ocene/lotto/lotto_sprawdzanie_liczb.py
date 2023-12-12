import random
wylosowanaLiczba = -1
wybranaLiczba=-1
listaUsera = [0,0,0,0,0,0,0]
listaLotto= [0,0,0,0,0,0,0]
ilePoprawnych = "nie wiem"

def zczytywanieLiczbOdUzytkownika(listaUsera):
    numerListy1 = 0
    while numerListy1 <7:
        wybranaLiczba = int(input("Podaj", numerListy1+1, "liczbe"))
        listaUsera[numerListy1] = wylosowanaLiczba
        numerListy1= numerListy1+1
        listaUsera.sort()
    return listaUsera

def losowanieLiczby(listaLotto):
    numerListy2 = 0
    while numerListy2 <7:
        wylosowanaLiczba = random.randint(1,49)
        listaLotto[numerListy2] = wylosowanaLiczba
        numerListy2= numerListy2+1
        listaLotto.sort()
    return listaLotto

def sprdzanieWygranej(ilePoprawnych):
    if listaLotto == listaUsera:
        ilePoprawnych = 6
        print("Gratulacje, udalo ci sie trafic wszystkie liczby")
    else:
        if

zczytywanieLiczbOdUzytkownika(listaUsera)
losowanieLiczby(listaLotto) 