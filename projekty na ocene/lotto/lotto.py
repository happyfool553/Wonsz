import random
import time
ileKont = 0

print("Witaj w punkcie lotto! ")
kontotaknie = input("Czy grales juz kiedys w nasze lotto? (tak/nie)")
if kontotaknie=="nie":
    f=open("lotto_liczba_kont.txt", "r")
    ileKont(f.read(1))
    print (ileKont)
    nowaNazwa = input("Jak chcesz nazwac swoje konto?")
    