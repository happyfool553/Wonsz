import random
wylosowanaLiczba = -1
wybranaLiczba=-1
listaUsera = [0,0,0,0,0,0,0]
listaLotto= [0,0,0,0,0,0,0]

def zczytywanieLiczbOdUzytkownika(listaUsera):
    numerListyUzytkownika = 0
    numerRundy = numerListyUzytkownika=1
    while numerListyUzytkownika <7:
        wybranaLiczba = int(input("Podaj liczbe", numerRundy))
        listaUsera[numerListyUzytkownika] = wybranaLiczba
        numerListyUzytkownika= numerListyUzytkownika+1
    return listaUsera

def losowanieLiczby(listaLotto):
    numerListyLotto = 0
    while numerListyLotto <7:
        wylosowanaLiczba = random.randint(1,49)
        listaLotto[numerListyLotto] = wylosowanaLiczba
        numerListyLotto= numerListyLotto+1
    return listaLotto
 
'''def sprdzanieWygranej(ilePoprawnych):
    if listaLotto == listaUsera:
        ilePoprawnych = 6
        print("Gratulacje, udalo ci sie trafic wszystkie liczby")
    else:
        print("Udalo ci sie trafic f{ilePoprawnych}")'''

zczytywanieLiczbOdUzytkownika(listaUsera)
losowanieLiczby(listaLotto) 