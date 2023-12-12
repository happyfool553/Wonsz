#importowanie bibliotek = fukcji

import random
los = random.randint(1,20) 
#w nawiasach jest zakres liczb, 1 i 20  wchodza w jego sklad


print(los)

import math
potega = math.pow(2,3)
print (potega)

suma = 2+5
roznica = 9-8
iloczyn = 7*8
iloraz = 6/3
potega = 3**2
modulo = 5%2

''' ifyyyyyy'''

liczba = int(input("podaj liczbe"))

if liczba > 0:
    print("Liczba jest wieksza od zera")
elif liczba <0:
    print("Liczba mniejsza od 0")
else:
    print("liczba jest rowna zero")


'''petleeeeee'''

for i in range(3):
    print("Numer: ", i)

#petle numerowane od zera!!!

for i in range (1,100):
    if i%2==0:
        print(i)
#zbior prawostronnie otwarty -> 100 nie wchodzi w sklad


for i in range(1,101, 2):
    print(i)

#to dwa zwieksza i o dwa a nie o jeden

for i in range(100,1, -1):
    print(i)
#mozna zmniejszac i 


for litera in "slowo":
    if litera == "o":
        break 
    print(litera)

#break przerywa dzialanie petli


for litera in "slowo":
    if litera == "o":
        continue 
    print(litera)

#continiue skipuje do nastepnej litery


while liczba <0:
    liczba = int(input("Podaj liczbe jeszcze raz:"))

    #liczba musi sie zmieniac, ineczej bedzie to petla nieskonczona!!