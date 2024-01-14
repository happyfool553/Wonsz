import time
odp_gr=""
nr_pytania=1
print("\nWitaj! Przed toba quiz, ktory ma na celu zaproponowanie ci piosenke zespolu Tomorrow X Together \nna podstawie twoich preferencji. \nPrzed toba kilkanascie pytan - po kazdej proponowanej odpowiedzi to, co masz wpisac do konsoli \nbedzie zapisane w ten sposob: (odpowiedz). \nJesli wpiszesz cos innego, niz powinienes - nie martw sie! Pytanie wyswietli sie jeszcze raz, \na ty bedziesz mogl spokojnie odpowiedziec na pytanie.\nMilego quizowania!\n")
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

#print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)
# 11111111111111111111111111111111111111111111111
while odp_gr !="w"or odp_gr !="bbv"or odp_gr !="mp":
    odp_gr= input("1. Lubisz wesole, pozytywnie brzmiace piosenki (w), te o mniej pozytywnym nastroju (mp) \nczy moze dajacy  *bad boy/girl* vibe (bbv)?\n")
    odp_gr=odp_gr.lower()
    if odp_gr =="w"or odp_gr =="bbv"or odp_gr =="mp":
        break
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
#print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

#2222222222222222222222222222222222222222222
while odp_gr !="sm"or odp_gr !="sp"or odp_gr !="o" or odp_gr!="c":
    odp_gr= input("2.Ktora z podanych czynnosci lubisz najbardziej? Sluchanie muzyki(sm), spanie(sp), \nogladanie seriali lub fimow(o), czy czytanie(c)?\n")
    odp_gr=odp_gr.lower()
    if odp_gr =="sm"or odp_gr =="sp"or odp_gr =="o"or odp_gr =="c":
        break
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
#print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

#33333333333333333333333333333333333333
while odp_gr !="f"or odp_gr !="b"or odp_gr !="g" or odp_gr !="zi" or odp_gr !="zo" or odp_gr !="cz" or odp_gr !="r":
    odp_gr= input("3.Jaki jest twoj ulubiony kolor z podanych? Fioletowy(f),  blekitny(b), granatowy(g), \nzielony(zi), zolty (zo), czerwony(cz), czy rozowy(r)?\n")
    odp_gr=odp_gr.lower()
    if odp_gr =="f"or odp_gr =="b"or odp_gr =="g" or odp_gr =="zi" or odp_gr =="zo" or odp_gr =="cz" or odp_gr =="r":
        break
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
#print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

#444444444444444444444444444
while odp_gr !="w"or odp_gr !="l"or odp_gr !="j" or odp_gr!="z":
    odp_gr= input("4. Ktora z por roku jest twoja ulubiona? Wiosna(w), lato(l), jesien(j), czy zima(z)?\n")
    odp_gr=odp_gr.lower()
    if odp_gr =="w"or odp_gr =="l"or odp_gr =="j" or odp_gr=="z":
        break
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
#print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)

#5555555555555555555555555555
while odp_gr !="s"or odp_gr !="pd"or odp_gr !="c" or odp_gr=="ps" or odp_gr=="w":
    odp_gr= input("5. Najbardziej wolisz, gdy jest slonecznie(s), pada deszcz(pd), pochmurnie(c), \npada snieg(ps), czy wieje(w)?\n")
    odp_gr=odp_gr.lower()
    if odp_gr =="s"or odp_gr =="pd"or odp_gr =="c" or odp_gr =="ps" or odp_gr =="w":
        break
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
#print(CROWN, run_away,cant_you_see_me,blue_hour,lovesong,magic,gbgb,srr,ctf,LEveL)


piosenki={
    CROWN:"CROWN",
    run_away:"9 and Three Quarters (Run Away)",
    cant_you_see_me:"Can't You See Me?",
    blue_hour:"Blue Hour",
    lovesong:"0X1=Lovesong (I Know I love You)",
    magic:"Magic",
    gbgb:"Good Boy Gone Bad",
    srr:"Sugar Rush Ride",
    ctf:"Chasing that feeling",
    LEveL:"LEveL"
}

if CROWN== 5 or run_away == 5 or cant_you_see_me==5 or blue_hour==5 or magic==5 or gbgb==5 or srr==5 or ctf==5 or LEveL==5:
    print("Proponowana piosenka dla ciebie to: "+piosenki[5])
elif CROWN== 4 or run_away == 4 or cant_you_see_me==4 or blue_hour==4 or magic==4 or gbgb==4 or srr==4 or ctf==4 or LEveL==4:
    print("Proponowana piosenka dla ciebie to: "+piosenki[4])
elif CROWN== 3 or run_away == 3 or cant_you_see_me==3 or blue_hour==3 or magic==3 or gbgb==3 or srr==3 or ctf==3 or LEveL==3:
    print("Proponowana piosenka dla ciebie to: "+piosenki[3])
elif CROWN== 2 or run_away == 2 or cant_you_see_me==2 or blue_hour==2 or magic==2 or gbgb==2 or srr==2 or ctf==2 or LEveL==2:   
    print("Proponowana piosenka dla ciebie to: "+piosenki[2])
elif CROWN== 1 or run_away == 1 or cant_you_see_me==1 or blue_hour==1 or magic==1 or gbgb==1 or srr==1 or ctf==1 or LEveL==1:    
    print("Proponowana piosenka dla ciebie to: "+piosenki[1])
time.sleep(2)
print("\nDziekuje za wypelnienie mojego quizu! \np.s. Jesli masz problem ze znalezieniem swojej piosenki, tutaj jest link do playlisty z wszystkimi mozliwymi wynikami <3\nhttps://open.spotify.com/playlist/5BROjp3oYoqqGjV9pzJWyq?si=08cddc00b08040f8 ")
#print(piosenki.keys())
#print(piosenki.values())



#print("Piosenki"+ int(CROWN)+int(run_away)+int(cant_you_see_me)+int(blue_hour)+int(lovesong)+int(magic)+int(gbgb)+int(srr)+int(ctf)+int(LEveL))
