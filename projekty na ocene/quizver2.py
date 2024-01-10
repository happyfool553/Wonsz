
odp_gr = "."

print("Witaj Przed toba quiz, ktory ma na calu zaproponowac ci piosenke zespolu Tomorrow X Together, na podstawie twoich preferencji. \nPrzed toba kilkanascie pytan - po kazdej proponowanej odpowiedzi to, co masz wpisac do konsoli bedzie zapisane w ten sposob (odpowiedz). \nMilego quizowania!")
#tworzenie slownika
piosenki={
    "CROWN": 0,
    "9 and Three Quarters (Run Away)":  0,
    "Can't You See Me?":0,
    "Blue Hour": 0,
    "0X1=Lovesong (I Know I love You)": 0,
    "Magic": 0,
    "Good Boy Gone Bad": 0,
    "Sugar Rush Ride": 0,
    "Chasing that feeling": 0,
    "LEveL": 0
}
#tworzenie zmiennych
CROWN= 0
run_away =  0
cant_you_see_me = 0
blue_hour = 0
lovesong = 0
magic = 0
gbgb= 0
srr= 0
ctf= 0
LEveL= 0

print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)
print("1. Pytania o twoj ULUBIONY nastroj piosenek")
odp_gr= input("Czy lubisz wesole, pozytywnie brzmiace piosenki (w), te o mniej pozytywnym nastroju (mp) czy moze dajacy *bad boy/girl* vibe (bbv)?")
if odp_gr == "w" or odp_gr == "W":
    CROWN= +1
    blue_hour= +1
    lovesong =+1
    magic= +1
    srr= +1
    ctf= +1
    LEveL= +1
elif   odp_gr == "bbv" or odp_gr=="BBV":   
    gbgb= +1   
elif odp_gr == "mp":
    run_away=+1
    cant_you_see_me=+1
else:
    print("Wyglada na to, ze wpisalxs cos innego, bylo napisane w poleceniu. Niestety, musisz rozpoczac quiz od poczatku :()")


print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)   
#print(piosenki.keys())
#print(piosenki.values())
#print("Piosenki"+ int(CROWN)+int(run_away)+int(cant_you_see_me)+int(blue_hour)+int(lovesong)+int(magic)+int(gbgb)+int(srr)+int(ctf)+int(LEveL))


