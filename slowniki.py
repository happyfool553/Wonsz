'''4.11.23            slownikiiiiiiii                   '''

kontakty= {}
kontakty["Jan"] = 123456789
kontakty["Jacek"] = 1234567890

kontakty={
    "Jan": 123456789,
    "Jacek":  1234567890,
    "Janusz":92345678
}
#wyswietlanie petli
print(kontakty["Jan"])

for imie, numer in kontakty.items():
    print("%s ma numer: %d" %(imie, numer))
    #  %s i %d odwoluje sie do tego ^^
    #najpierw klucz (imie) a pozniej wartosc

print(kontakty.keys())
print(kontakty.values())

#usuwanie jednego
del kontakty["Jacek"]


'''        zlozonosc        '''
lista = [1,2,3,4,5,6,7,8,9]

for i in lista:
    print (i)
#liczenie jak szybko robi sie program
import time
start = time.time()
lista = [1,2,3,4,5,6,7,8,9,12,13,43,33,45,56,67,678,89,89,]
for i in lista:
    print (i)

end=time.time()
print(end-start)


n=int(input("podaj liczbe calkowita"))
start2 = time.time()
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()
end2=time.time()
print(end-start)





