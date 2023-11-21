import random

#twozrenie zmiennych miejsc
lista = [1,2,3,4,5,6,7,8,9]
wybranaliczba = ""

def powitanie():
    print("Witaj!Zagrajmy w kolko i krzyzyk. \n ")
    print("Zasady sa proste - wybierasz miejsce w ktorym chcesz postawic kolko i dazysz, by ustawic 3 kola pod rzad. Powodzenia!")



def ruchgracza():    
    print("Wybierz miejsce, w ktorym chcesz wstawic swoj znak")
    print("" ,lista[0],"/", lista[1],"/",lista[2],"\n", lista[3],"/", lista[4],"/", lista[5],"\n", lista[6],"/", lista[7],"/", lista[8])
    wybranaliczba = int(input("Wpisz liczbe od 1 do 9 "))
      
    numerwliscie = (wybranaliczba - 1)
    lista[numerwliscie] = "o"
    print("" ,lista[0],"/", lista[1],"/",lista[2],"\n", lista[3],"/", lista[4],"/", lista[5],"\n", lista[6],"/", lista[7],"/", lista[8])
   
def ruchbota():
    print("Teraz moja runda!")
    def losowanieruchu():
        losbota = random.randint(0,8)
        if losbota=="o" or losbota=="x":
            losowanieruchu()
        else: 
            ruchbota=(losbota-1)
            lista[ruchbota] = "x"
            print("" ,lista[0],"/", lista[1],"/",lista[2],"\n", lista[3],"/", lista[4],"/", lista[5],"\n", lista[6],"/", lista[7],"/", lista[8])
    losowanieruchu()        

def sprawdanie_wygranej_gracza():
    if lista[0]==lista[1]==lista[2]:

        if lista[0]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[3]==lista[4]==lista[5]:
        if lista[3]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[6]==lista[7]==lista[8]:
        if lista[6]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[0]==lista[4]==lista[8]:
        if lista[0]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[2]==lista[4]==lista[6]:
        if lista[2]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[0]==lista[3]==lista[6]:
        if lista[0]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[1]==lista[4]==lista[7]:
        if lista[1]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[2]==lista[5]==lista[8]:
        if lista[2]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
def sprawdanie_wygranej_bota():
    if lista[0]==lista[1]==lista[2]:

        if lista[0]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[3]==lista[4]==lista[5]:
        if lista[3]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[6]==lista[7]==lista[8]:
        if lista[6]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[0]==lista[4]==lista[8]:
        if lista[0]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[2]==lista[4]==lista[6]:
        if lista[2]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[0]==lista[3]==lista[6]:
        if lista[0]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    if lista[1]==lista[4]==lista[7]:
        if lista[1]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")   
    if lista[2]==lista[5]==lista[8]:
        if lista[2]=="o":
            print("Wygales")
        else:
            print("Udalo mi sie wygrac!")
    else: jedna_runda()
def jedna_runda():
    ruchgracza()
    sprawdanie_wygranej_gracza()
    ruchbota()
    sprawdanie_wygranej_bota()
powitanie()
jedna_runda()





