print("\nWitaj w kalulatorze jednostek!\n")
print("Mozliwe jednostki, ktore sa do wyboru to: \nkilometry(km), metry(m), centymetry(cm), milimetry(mm)\nkilogramy(kg), dekagram(dag), gramy(g),\nlitry(l), mililitry(ml)")

liczba = int(input("\nWpisz liczbe (ilosc):  "))
jedn_wpr=input("Wybierz jednostke, z ktorej chesz przekonwertowac (wpisz skrotowo, tak jak jest napisane w nawiasach):  ")
jedn_wpr=jedn_wpr.lower()

while jedn_wpr !="km" or jedn_wpr !="m" or jedn_wpr !="cm" or jedn_wpr !="m" or jedn_wpr !="kg"or jedn_wpr !="dag" or jedn_wpr !="g" or jedn_wpr !="l"or jedn_wpr !="ml":
    if jedn_wpr =="km" or jedn_wpr =="m" or jedn_wpr =="cm" or jedn_wpr =="m" or jedn_wpr =="kg"or jedn_wpr =="dag" or jedn_wpr =="g" or jedn_wpr =="l"or jedn_wpr =="ml":
        break
    jedn_wpr=input("Wybierz jednostke, z ktorej chesz przekonwertowac (wpisz skrotowo, tak jak jest napisane w nawiasach):  ")
    jedn_wpr=jedn_wpr.lower()
    
if jedn_wpr =="km"or jedn_wpr =="m" or jedn_wpr =="cm" or jedn_wpr =="mm":    
    jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(kilometry(km), metry(m), centymetry(cm), milimetry(mm)):  ")
    jedn_wypr=jedn_wypr.lower()
    while jedn_wypr !="km"or jedn_wypr !="m" or jedn_wypr !="cm" or jedn_wypr !="m":
        if jedn_wypr =="km"or jedn_wypr =="m" or jedn_wypr =="cm" or jedn_wypr =="m":
            break
    jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(kilometry(km), metry(m), centymetry(cm), milimetry(mm)):  ")
    jedn_wypr=jedn_wypr.lower() 
    

           
    
#if jedn_wpr =="kg"or jedn_wpr =="dag" or jedn_wpr =="g":
#    jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(kilogramy(kg), dekagram(dag), gramy(g)):  ")
    
#if jedn_wpr =="l"or jedn_wpr =="ml" :
#    jedn_wypr=input("Wybierz jednostke, na ktora chesz przekonwertowac(litry(l), mililitry(ml)):  ")    
 
    
