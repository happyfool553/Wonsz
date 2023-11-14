#30.01.2023
liczba = -1
petla2 = "tak"

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

while petla2=="tak":
        if petla2 =="tak":
            kalkulator()
            petla2 = input("Czy chcesz wykonac nastepne dzialanie? (tak/nie) ")
        elif petla2=="nie":
            print("Dziekujemy za uzycie naszego kalkulatora!")

                       
print("Przepraszam, nie obsluguje takiej komendy")
