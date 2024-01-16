import random
wylosowanaLiczba = -1
wybranaLiczba=-1
listaUsera = [-5,-4,-3,-2,-1,0]
listaLotto= [0,0,0,0,0,0]
ilePoprawnych = 0
 

numerListyUzytkownika = 0
while numerListyUzytkownika <6:
    while listaUsera[0]!=listaUsera[numerListyUzytkownika] and listaUsera[1]!=listaUsera[numerListyUzytkownika]and listaUsera[2]!=listaUsera[numerListyUzytkownika] and listaUsera[3]!=listaUsera[numerListyUzytkownika] and listaUsera[4]!=listaUsera[numerListyUzytkownika]and listaUsera[5]!=listaUsera[numerListyUzytkownika]:
        wybranaLiczba = int(input("Podaj liczbe od 1 do 49  "))
    listaUsera[numerListyUzytkownika] = wybranaLiczba
    numerListyUzytkownika= numerListyUzytkownika+1
print(listaUsera)

 

numerListyLotto = 0
while numerListyLotto <6:
    wylosowanaLiczba = random.randint(1,49)
    listaLotto[numerListyLotto] = wylosowanaLiczba
    numerListyLotto= numerListyLotto+1
print(listaLotto)

 
 

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

 

if listaLotto == listaUsera:
    ilePoprawnych = 6
    print("Gratulacje, udalo ci sie trafic wszystkie liczby")
else:
    print("Udalo ci sie trafic f{ilePoprawnych}")
