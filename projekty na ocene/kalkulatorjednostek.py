print("\nWitaj w kalulatorze jednostek!\n")
print("Mozliwe jednostki, ktore sa do wyboru to: \nkilometry(km), metry(m), centymetry(cm), milimetry(mm), rok swietlny (ly)\nbit (b), bajt (bb), kilobit (kb), megabit(mb), gigabit (gb), kilobajt (kbb), megabajt(mmbb), gigabajt (ggbb), terabajt(ttbb)")

liczba = int(input("\nWpisz liczbe (ilosc):  "))
jedn_wpr=input("Wybierz jednostke, z ktorej chesz przekonwertowac (wpisz skrotowo, tak jak jest napisane w nawiasach):  ")
jedn_wpr=jedn_wpr.lower()

while jedn_wpr !="km" or jedn_wpr !="m" or jedn_wpr !="cm" or jedn_wpr !="mm" or jedn_wpr !="ly"    or jedn_wpr !="b"or jedn_wpr !="bb" or jedn_wpr !="kb" or jedn_wpr !="mb"or jedn_wpr !="gb" or jedn_wpr !="kbb" or jedn_wpr !="mmbb" or jedn_wpr !="ggbb" or jedn_wpr !="ttbb":
    if jedn_wpr =="km" or jedn_wpr =="m" or jedn_wpr =="cm" or jedn_wpr =="mm" or jedn_wpr =="ly"   or jedn_wpr =="b"or jedn_wpr =="bb" or jedn_wpr =="kb" or jedn_wpr =="mb"or jedn_wpr =="gb" or jedn_wpr =="kbb" or jedn_wpr =="mmbb" or jedn_wpr =="ggbb" or jedn_wpr =="ttbb":
        break
    jedn_wpr=input("Wybierz jednostke, z ktorej chesz przekonwertowac (wpisz skrotowo, tak jak jest napisane w nawiasach):  ")
    jedn_wpr=jedn_wpr.lower()
    
if jedn_wpr =="km"or jedn_wpr =="m" or jedn_wpr =="cm" or jedn_wpr =="mm" or jedn_wpr =="ly":    
    jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(kilometry(km), metry(m), centymetry(cm), milimetry(mm)):  ")
    jedn_wypr=jedn_wypr.lower()
    while jedn_wypr !="km"or jedn_wypr !="m" or jedn_wypr !="cm" or jedn_wypr !="m":
        if jedn_wypr =="km"or jedn_wypr =="m" or jedn_wypr =="cm" or jedn_wypr =="m":
            break
        jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(kilometry(km), metry(m), centymetry(cm), milimetry(mm)):  ")
        jedn_wypr=jedn_wypr.lower() 
    
    if jedn_wpr=="km":
        print (liczba, "kilometrow to")
        if jedn_wypr=="m": 
            liczba = liczba*1000
            print( liczba, "m")
        elif jedn_wypr=="cm":
            liczba = liczba*100000
            print( liczba, "cm")
        elif jedn_wypr=="mm":
            liczba = liczba*1000000
            print(liczba, "mm")
    elif jedn_wpr=="m":
        print (liczba, "metrow to")
        if jedn_wypr=="km": 
            liczba = liczba/1000
            print( liczba, "km")
        elif jedn_wypr=="cm":
            liczba = liczba*100
            print(liczba, "cm")
        elif jedn_wypr=="mm":
            liczba = liczba*1000
            print(liczba, "mm")
    elif jedn_wpr=="cm":
        print (liczba, "centymetrow to")
        if jedn_wypr=="km": 
            liczba = liczba*0.00001
            print("Twoja liczba to", liczba, "km")
        elif jedn_wypr=="m":
            liczba = liczba/100
            print("Twoja liczba to", liczba, "mm")
        elif jedn_wypr=="mm":
            liczba = liczba*10
            print("Twoja liczba to", liczba, "mm")
    elif jedn_wpr=="mm":
        print (liczba, "milimetrow to")
        if jedn_wypr=="km": 
            liczba = liczba*0.000001
            print( liczba, "km")
        elif jedn_wypr=="m":
            liczba = liczba*0.001
            print( liczba, "m")
        elif jedn_wypr=="cm":
            liczba = liczba*0.1
            print( liczba, "cm")
    elif jedn_wpr=="ly":
        print (liczba, "lat swietlnych to")
        if jedn_wypr=="km": 
            liczba = liczba*9460528436447.5
            print( liczba, "km")
        elif jedn_wypr=="m":
            liczba = liczba*9460528436447500
            print(liczba, "m")
        elif jedn_wypr=="cm":
            liczba = liczba*946052843644750000
            print(liczba, "cm")
        elif jedn_wypr=="mm":
            liczba = liczba*9460528436447500000
            print(liczba, "mm")
        
elif jedn_wpr =="b"or jedn_wpr =="bb" or jedn_wpr =="kb" or jedn_wpr =="mb"or jedn_wpr =="gb" or jedn_wpr =="kbb" or jedn_wpr =="mmbb" or jedn_wpr =="ggbb" or jedn_wpr =="ttbb":
    jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(bit (b), bajt (bb), kilobit (kb), megabit(mb), gigabit (gb), kilobajt (kbb), megabajt( mmbb), gigabajt (ggbb), terabajt(ttbb)):   ")
    jedn_wypr=jedn_wypr.lower()
    while jedn_wpr !="b"or jedn_wpr !="bb" or jedn_wpr !="kb" or jedn_wpr !="mb"or jedn_wpr !="gb" or jedn_wpr !="kbb" or jedn_wpr !="mmbb" or jedn_wpr !="ggbb" or jedn_wpr !="ttbb":
        if jedn_wpr =="b"or jedn_wpr =="bb" or jedn_wpr =="kb" or jedn_wpr =="mb"or jedn_wpr =="gb" or jedn_wpr =="kbb" or jedn_wpr =="mmbb" or jedn_wpr =="ggbb" or jedn_wpr =="ttbb":
            break
        jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(bit (b), bajt (bb), kilobit (kb), megabit(mb), gigabit (gb), kilobajt (kbb), megabajt( mmbb), gigabajt (ggbb), terabajt(ttbb)):   ")
        jedn_wypr=jedn_wypr.lower() 
    if jedn_wpr=="b":
        print (liczba, "bitow to ")
        if jedn_wypr=="b":
            print(liczba, "bitow")
        elif jedn_wypr=="bb":
            liczba = liczba *0.125
            print(liczba, "bajtow")
        elif jedn_wypr=="kb":
            liczba = liczba *0.001
            print(liczba, "kilobitow")
        elif jedn_wypr=="mb":
            liczba = liczba *0.001
            print(liczba, "megabitow")
        elif jedn_wypr=="gb":   
            liczba = liczba *0.001
            print(liczba, "gigabitow")
        elif jedn_wypr=="kbb": 
            liczba = liczba *0.001
            print(liczba, "megabitow")   
        #elif jedn_wypr=="mmbb":    
        #elif jedn_wypr=="ggbb":    
        #elif jedn_wypr=="ttbb":
        
        
    #elif jedn_wpr=="bb":
    #elif jedn_wpr=="kb":
    #elif jedn_wpr=="mb":
    #elif jedn_wpr=="gb":    
    #elif jedn_wpr=="kbb":    
    #elif jedn_wpr=="mmbb":    
    #elif jedn_wpr=="ggbb":    
    #elif jedn_wpr=="ttbb":
  
# b bb kb mb gb kbb mmbb ggbb ttbb
# https://www.naukowiec.org/kalkulatory/pamiec.html
#Bit (b), bajt (bb), kilobit (kb), megabit(mb), gigabit (gb), kilobajt (kbb), megabajt( mmbb), gigabajt (ggbb), terabajt(ttbb)




    '''if jedn_wypr=="b":
    elif jedn_wypr=="bb":
    elif jedn_wypr=="kb":
    elif jedn_wypr=="mb":
    elif jedn_wypr=="gb":    
    elif jedn_wypr=="kbb":    
    elif jedn_wypr=="mmbb":    
    elif jedn_wypr=="ggbb":    
    elif jedn_wypr=="ttbb":'''
