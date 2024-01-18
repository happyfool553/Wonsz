
#dodawanie peselu
#filepath = "pesel.txt"
#f=open(filepath, "a")
#dod_pesel=input("Podaj swoj PESEL, ktory chcesz dodac do naszej bazy danych")
#f.write("1234")

#a - append (do edytowania)
#f.close()



krok1=input(print("Chcesz dodac, czy sprawdzic swoj pesel?(dodac/sprawdzic)"))
krok1=krok1.lower
krok1=="dodac"
#while krok1!="dodac" or krok1!="sprawdzic":
#    if krok1=="dodac" or krok1=="sprawdzic":
#        break
#    krok1=input(print("Chcesz dodac, czy sprawdzic swoj pesel?(dodac/sprawdzic)"))
#    krok1=krok1.lower


if krok1=="dodac":   
    file=open('pesel.txt', 'a')
    #dod_pesel=input("Podaj swoj PESEL, ktory chcesz dodac do naszej bazy danych")
    file.write("1234")
    file.close() 
elif krok1 =="sprawdzic":
    spr_pesel=input("Podaj PESEL, ktory bedziesz chcialx sprawdzic:  ")
    
    

