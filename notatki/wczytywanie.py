'''21.11.23'''

f=open("text.txt", "r")
print(f.read())
f.close()
#r - read (wyswietlanie)
#trzeba zamykac bazy danych i txt

for i in f:
    print("Linijka: ", i)


f=open("text.txt", "a")
f.write("\neeeee\n")
#a - append (do edytowania)
f.close()

