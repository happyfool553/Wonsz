
odp_gr = " "
nr_pytania=1
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


def pytanie1():
    odp_gr= input("1. Czy lubisz wesole, pozytywnie brzmiace piosenki (w), te o mniej pozytywnym nastroju (mp) czy moze dajacy *bad boy/girl* vibe (bbv)?")
def ptk1():
    if odp_gr == "w" :
        CROWN= CROWN+1
        blue_hour= blue_hour+1
        lovesong =lovesong+1
        magic= magic+1
        srr= srr+1
        ctf= ctf+1
        LEveL= LEveL+1
    elif   odp_gr == "bbv":   
        gbgb= gbgb+1   
    elif odp_gr == "mp":
        run_away= run_away+1
        cant_you_see_me=cant_you_see_me+1
    else:
        print("Wyglada na to, ze wpisalxs cos innego, bylo napisane w poleceniu. Twoja odpowiedz z tego pytania nie bedzie brana pod uwage w punktacji!")
    print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

def pytanie2():
    odp_gr= input("2.Ktora z podanych czynnosci lubisz najbardziej? sluchanie muzyki(sm), spanie(sp), ogladanie seriali lub fimow(o), czytanie(c)")
#text.lower(odp_gr)
def ptk2():
    if odp_gr=="sm":
        magic =magic+1
        srr=srr+1
    elif odp_gr=="sp":
        cant_you_see_me=cant_you_see_me+1
    elif odp_gr=="o":
        gbgb=gbgb+1
        ctf=ctf+1
        LEveL=LEveL+1
    elif odp_gr=="c":
        lovesong=lovesong+1
        CROWN=CROWN+1
        run_away=run_away+1
        blue_hour=blue_hour+1
    else:
        print("Wyglada na to, ze wpisalxs cos innego, bylo napisane w poleceniu. Twoja odpowiedz z tego pytania nie bedzie brana pod uwage w punktacji!")
    print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

def pytanie3(): 
    odp_gr= input("3.Jaki jest twoj ulubiony kolor z podanych? Fioletowy(f),  blekitny(b), granatowy(g), zielony(zi), zolty (zo), czerwony(cz), rozowy(r)")
def ptk3():
    if odp_gr=="f":
        cant_you_see_me=cant_you_see_me+1
    elif odp_gr=="b":
        blue_hour=blue_hour+1
        magic=magic+1
    elif odp_gr=="g":
        lovesong=lovesong+1
        ctf=ctf+1
    elif odp_gr=="zi":
        run_away=run_away+1
        LEveL=LEveL+1
    elif odp_gr=="zo":
        CROWN=CROWN=+1
    elif odp_gr=="cz":
        gbgb=gbgb+1
    elif odp_gr=="r":
        srr=srr+1
    else:
        print("Wyglada na to, ze wpisalxs cos innego, bylo napisane w poleceniu. Twoja odpowiedz z tego pytania nie bedzie brana pod uwage w punktacji!")
    print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

def pytanie4():
    odp_gr= input("4. Ktora z por roku jest twoja ulubiona? Wiosna(w), lato(l), jesien(j), czy zima(z)?")
def ptk4():
    if odp_gr=="w":
        blue_hour=blue_hour+1
    elif odp_gr=="l":
        CROWN=CROWN+1
        magic=magic+1
        srr=srr+1
    elif odp_gr=="j":
        run_away=run_away+1
        cant_you_see_me=cant_you_see_me+1
        gbgb=gbgb+1
        LEveL=LEveL+1
    elif odp_gr=="z":
        lovesong=lovesong+1
        ctf=ctf+1
    else:
        print("Wyglada na to, ze wpisalxs cos innego, bylo napisane w poleceniu. Twoja odpowiedz z tego pytania nie bedzie brana pod uwage w punktacji!")
    print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

def pytanie5():
    odp_gr= input("5. Najbardziej wolisz, gdy jest slonecznie(s), pada deszcz(pd), pochmurnie(c), pada snieg(ps), czy wieje(w)")
def ptk5():
    if odp_gr=="s":
        CROWN=CROWN+1
        blue_hour=blue_hour+1
        magic=magic+1
        srr=srr+1
    elif odp_gr=="pd":
        run_away=run_away+1
        lovesong+lovesong+1
    elif odp_gr=="c":
        cant_you_see_me=cant_you_see_me+1
        gbgb=gbgb+1
    elif odp_gr=="ps":
        blue_hour=blue_hour+1
        ctf=ctf+1
        LEveL=LEveL+1
    elif odp_gr=="w":
        cant_you_see_me=cant_you_see_me+1
        LEveL=LEveL+1
        gbgb=gbgb+1
    else:
        print("Wyglada na to, ze wpisalxs cos innego, bylo napisane w poleceniu. Twoja odpowiedz z tego pytania nie bedzie brana pod uwage w punktacji!")
    print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)



#print(piosenki.keys())
#print(piosenki.values())
#print("Piosenki"+ int(CROWN)+int(run_away)+int(cant_you_see_me)+int(blue_hour)+int(lovesong)+int(magic)+int(gbgb)+int(srr)+int(ctf)+int(LEveL))


