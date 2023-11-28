import random
import time
#            bledy do naprawienia: nie konczy grym gdy ktos wygrywa; bardzo latwo wygrac z nim
#twozrenie zmiennych miejsc
lista = [1,2,3,4,5,6,7,8,9]
wybranaliczba = ""
w_gracza = 0
w_bota= 0
numerwliscie = 10

def powitanie():
    print("Witaj!Zagrajmy w kolko i krzyzyk. \n ")
    print("Zasady sa proste - wybierasz miejsce w ktorym chcesz postawic kolko i dazysz, by ustawic 3 kola pod rzad. Powodzenia!")



def ruchgracza():    
    print("Teraz twoja runda. Wybierz miejsce, w ktorym chcesz wstawic swoj znak")
    print("" ,lista[0],"/", lista[1],"/",lista[2],"\n", lista[3],"/", lista[4],"/", lista[5],"\n", lista[6],"/", lista[7],"/", lista[8])

    wybranaliczba = int(input("Wybierz liczbe od 1 do 9 "))
    numerwliscie = wybranaliczba - 1
    lista[numerwliscie] = "o"
    print("" ,lista[0],"/", lista[1],"/",lista[2],"\n", lista[3],"/", lista[4],"/", lista[5],"\n", lista[6],"/", lista[7],"/", lista[8])
    time.sleep(2)
         
   
def ruchbota():
    print("Teraz moja runda!")
    time.sleep(1)
    def losowanieruchu():
        losbota = random.randint(0,8)
        if lista[losbota]=="o" or lista[losbota]=="x":
            losowanieruchu()
        else: 
            lista[losbota] = "x"
            print("" ,lista[0],"/", lista[1],"/",lista[2],"\n", lista[3],"/", lista[4],"/", lista[5],"\n", lista[6],"/", lista[7],"/", lista[8])
            time.sleep(2)
    losowanieruchu()        

def sprawdanie_wygranej():
    if lista[0]==lista[1]==lista[2]:

        if lista[0]=="o":
            print("Wygales!")
            w_gracza+=1

        else:
            print("Udalo mi sie wygrac!")
            w_bota+= 1
    if lista[3]==lista[4]==lista[5]:
        if lista[3]=="o":
            print("Wygales")
            w_gracza =1
        else:
            print("Udalo mi sie wygrac!")
            w_bota = 1
    if lista[6]==lista[7]==lista[8]:
        if lista[6]=="o":
            print("Wygales")
            w_gracza += 1
        else:
            print("Udalo mi sie wygrac!")
            w_bota+= 1
    if lista[0]==lista[4]==lista[8]:
        if lista[0]=="o":
            print("Wygales")
            w_gracza += 1
        else:
            print("Udalo mi sie wygrac!")
            w_bota+= 1
    if lista[2]==lista[4]==lista[6]:
        if lista[2]=="o":
            print("Wygales")
            w_gracza += 1
        else:
            print("Udalo mi sie wygrac!")
            w_bota+= 1
    if lista[0]==lista[3]==lista[6]:
        if lista[0]=="o":
            print("Wygales")
            w_gracza += 1
        else:
            print("Udalo mi sie wygrac!")
            w_bota+= 1
    if lista[1]==lista[4]==lista[7]:
        if lista[1]=="o":
            print("Wygales")
            w_gracza += 1
        else:
            print("Udalo mi sie wygrac!")
            w_bota+= 1
    if lista[2]==lista[5]==lista[8]:
        if lista[2]=="o":
            print("Wygales")
            w_gracza += 1
        else:
            print("Udalo mi sie wygrac!")
            w_bota+= 1

def zakonczenie():
    print("Dziekuje za gre, jesli chcesz zagrac jeszcze raz, uruchom pogram ponownie!") 


powitanie()
while w_gracza!=1 or w_bota!=1:
    ruchgracza()
    sprawdanie_wygranej()
    ruchbota()
    sprawdanie_wygranej()
zakonczenie()    








