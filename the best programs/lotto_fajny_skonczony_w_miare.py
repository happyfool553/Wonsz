import random
wylosowanaLiczba = -1
wybranaLiczba=-1
listaUsera = [0,0,0,0,0,0]
listaLotto= [0,0,0,0,0,0]
ilePoprawnych = 0
 
def zczytywanieLiczbOdUzytkownika(listaUsera):
    numerListyUzytkownika = 0
    while numerListyUzytkownika <6:
        wybranaLiczba = int(input("Podaj liczbe od 1 do 49  "))
        listaUsera[numerListyUzytkownika] = wybranaLiczba
        numerListyUzytkownika= numerListyUzytkownika+1
    print(listaUsera)
    return listaUsera
 
def losowanieLiczby(listaLotto):
    numerListyLotto = 0
    while numerListyLotto <6:
        wylosowanaLiczba = random.randint(1,49)
        listaLotto[numerListyLotto] = wylosowanaLiczba
        numerListyLotto= numerListyLotto+1
    print(listaLotto)
    return listaLotto
 
 
def defIlePoprawnych(ilePoprawnych):
    liczbaRund = 0
    while liczbaRund<6:
        if listaUsera[liczbaRund]==listaLotto[0]:
            ilePoprawnych=ilePoprawnych+1
        liczbaRund=liczbaRund+1
    liczbaRund = 0
    while liczbaRund<6:
        if listaUsera[liczbaRund]==listaLotto[1]:
            ilePoprawnych=ilePoprawnych+1
        liczbaRund=liczbaRund+1
    liczbaRund = 0
    while liczbaRund<6:
        if listaUsera[liczbaRund]==listaLotto[2]:
            ilePoprawnych=ilePoprawnych+1
        liczbaRund=liczbaRund+1
    liczbaRund = 0
    while liczbaRund<6:
        if listaUsera[liczbaRund]==listaLotto[3]:
            ilePoprawnych=ilePoprawnych+1
        liczbaRund=liczbaRund+1
    liczbaRund = 0
    while liczbaRund<6:
        if listaUsera[liczbaRund]==listaLotto[4]:
            ilePoprawnych=ilePoprawnych+1
        liczbaRund=liczbaRund+1
    liczbaRund = 0
    while liczbaRund<6:
        if listaUsera[liczbaRund]==listaLotto[5]:
            ilePoprawnych=ilePoprawnych+1
        liczbaRund=liczbaRund+1
    print(ilePoprawnych)
    return(ilePoprawnych)
 
def sprdzanieWygranej(ilePoprawnych):
    if listaLotto == listaUsera:
        ilePoprawnych = 6
        print("Gratulacje, udalo ci sie trafic wszystkie liczby")
    else:
        print("Udalo ci sie trafic f{ilePoprawnych}")
 
zczytywanieLiczbOdUzytkownika(listaUsera)
losowanieLiczby(listaLotto)
defIlePoprawnych(ilePoprawnych)