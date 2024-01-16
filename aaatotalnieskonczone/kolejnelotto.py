   
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
        if wybranaLiczba>=1 and wybranaLiczba<= 49 and wybranaLiczba!=listaUsera[0]and wybranaLiczba!=listaUsera[1]and wybranaLiczba!=listaUsera[2]and wybranaLiczba!=listaUsera[3]and wybranaLiczba!=listaUsera[4]and wybranaLiczba!=listaUsera[5]:
            listaUsera[numerListyUzytkownika] = wybranaLiczba 
        else:
            while wybranaLiczba<=1 or wybranaLiczba>= 49 or wybranaLiczba==listaUsera[0]or wybranaLiczba==listaUsera[1]or wybranaLiczba==listaUsera[2]or wybranaLiczba==listaUsera[3]or wybranaLiczba==listaUsera[4]or wybranaLiczba==listaUsera[5]:
                wybranaLiczba = int(input("Podaj liczbe od 1 do 49  "))
                if wybranaLiczba>=1 and wybranaLiczba<= 49 and wybranaLiczba!=listaUsera[0]and wybranaLiczba!=listaUsera[1]and wybranaLiczba!=listaUsera[2]and wybranaLiczba!=listaUsera[3]and wybranaLiczba!=listaUsera[4]and wybranaLiczba!=listaUsera[5]:
                    listaUsera[numerListyUzytkownika] = wybranaLiczba
                    break           
        numerListyUzytkownika= numerListyUzytkownika+1
    print(listaUsera)
    return listaUsera
 
def losowanieLiczby(listaLotto):
    numerListyLotto = 0
    while numerListyLotto <6:
        wylosowanaLiczba = random.randint(1,49)
        if wylosowanaLiczba!=listaLotto[0] and wylosowanaLiczba!=listaLotto[1] and wylosowanaLiczba!=listaLotto[2] and wylosowanaLiczba!=listaLotto[3] and wylosowanaLiczba!=listaLotto[4] and wylosowanaLiczba!=listaLotto[5]:
            listaLotto[numerListyLotto] = wylosowanaLiczba
        else:
            while wylosowanaLiczba==listaLotto[0] and wylosowanaLiczba==listaLotto[1] and wylosowanaLiczba==listaLotto[2] and wylosowanaLiczba==listaLotto[3] and wylosowanaLiczba==listaLotto[4] and wylosowanaLiczba==listaLotto[5]:
                wylosowanaLiczba = random.randint(1,49)
                if wylosowanaLiczba!=listaLotto[0] and wylosowanaLiczba!=listaLotto[1] and wylosowanaLiczba!=listaLotto[2] and wylosowanaLiczba!=listaLotto[3] and wylosowanaLiczba!=listaLotto[4] and wylosowanaLiczba!=listaLotto[5]:
                    listaLotto[numerListyLotto] = wylosowanaLiczba
                    break
        numerListyLotto= numerListyLotto+1
        
    print(listaLotto)
    return listaLotto
 
 
def IlePoprawnych(ilePoprawnych):
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
    if ilePoprawnych==6:
        print ("Gratulacje, udalo ci sie trafic wszystkie liczby")
    else:
        print("Udalo ci sie trafic",ilePoprawnych,"raz/y")
    return(ilePoprawnych)
 
#def sprdzanieWygranej(ilePoprawnych):
#    if listaLotto == listaUsera:
 #       ilePoprawnych = 6
  #      print("Gratulacje, udalo ci sie trafic wszystkie liczby")
    #else:
      #  print("Udalo ci sie trafic",ilePoprawnych,"raz/y")
 
zczytywanieLiczbOdUzytkownika(listaUsera)
losowanieLiczby(listaLotto)
IlePoprawnych(ilePoprawnych)
#sprdzanieWygranej(ilePoprawnych)