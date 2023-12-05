
def powitanie ():
    print("Czesc!")
#def nazwa (parametry)

powitanie()
#wywolywanie funkcji

def powitanie_imienne(imie):
    print("Czesc, ",imie)

powitanie_imienne("Jacek")
#Jacek to parametr imie

def dzielenie(dzielna, dzielnik):
    if dzielnik ==0:
        return "Nie dziel przez 0"
    else:
        return dzielna/dzielnik
    
print (dzielenie(5,2))
print (dzielenie(3,1))
iloraz = dzielenie (3,4)
print(iloraz)
#samo return zakancza 
'''listyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'''
lista = [1,2,3,9,5,7,4]
print(type(lista))

print(lista)
#print(*lista)               powinno dzialac lol ale wychodzi blad w obu
#print(*lista, sep=";")

#listy ->>> nawiazy kwardatowe!!!
#print(type(lista)) sprawdza typ zmiennej

lista.sort()
print(lista)
#sortuje

lista.reverse()
print(lista)
#odwraca

lista.sort(reverse=True)
print(lista)
#to tez odwraca

print(lista.count(3))
#liczy ilosc liczb o danej wartosci

lista.remove(3)
print(lista)
#usuwa dana liczbe

lista.append(1)
print(lista)
#dodaje dana liczbe


print(lista[0])
print(lista[5])
#printuje liczbe o danym miejscu - liczymy od zera!

print(len(lista))
#printuje jaka ma dlugosc 

lista[0] = 6
print(lista)
#zmienia wartosc danej liczby

for i in lista:
    print(i)

#wyprintuje nam wszystkie wartosci

'''tuple/krotki - nie mozna ich zmieniac''' 

krotka=(1,2,3)
print(krotka)

krotka2 = 1,2,3,2.5,"abc"
print(krotka2)

krotka3=("anbc",)
print(type(krotka3))
#krotka jedno elementowa

print(len(krotka2))
