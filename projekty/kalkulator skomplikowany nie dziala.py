#30.01.2023
liczba = -1

def taknie():
    petla2 = "tak"
    while petla2=="tak":

        kalkulator()
        petla2 = input("Czy chcesz wykonac nastepne dzialanie? (tak/nie) ")
        if petla2=="nie":
            print("Dziekujemy za uzycie naszego kalkulatora!")
        else:
            break
def kalkulator():
    a = int(input("Podaj liczbe a: "))
    dzialanie = input("Wybierz dzialanie: ")
    b = int(input("Podaj liczbe b: "))
    wynik = 0
    if dzialanie == "+":
        wynik = a+b
        print("Suma ", a, " i ", b, " jest rowna ", wynik)
    elif dzialanie == "-":
        wynik = a-b
        print("Roznica ", a, " i ", b, " jest rowna ", wynik)
    elif dzialanie == "*":
        wynik = a*b
        print("Iloczyn ", a, " i ", b, " jest rowny ", wynik)
    elif dzialanie == "/":
        if b!=0:
            wynik = a/b
            print("Iloraz ", a, " przez ", b, " jest rown ", wynik)
        else:
            print("Nie mozna dzielic przez zero")
    elif dzialanie == "**":
        wynik = a**b
        print( a, " do potegi ", b, " jest rowne ", wynik)
    elif dzialanie == "%":
        if b!=0:
            wynik = a%b
            print("Modulo ", a, " przez ", b, " jest rowne ", wynik)
        else:
            print("Nie mozna dzielic przez zero")
    else:
        print("Podaj inne dzialanie")


print("Przepraszam, nie obsluguje takiej komendy")
petla3 = input("Czy chcesz wrocic do kalkulatora? (tak/nie) ")
if petla3 == "tak":
    taknie()
else:
    print("Dziekujemy za uzycie naszego kalkulatora!")

taknie() 
    