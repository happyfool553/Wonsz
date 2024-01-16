
odp_gr = "."

print("Witaj Przed toba quiz, ktory ma na calu zaproponowac ci piosenke zaspolu Tomorrow X Together, na podstawie twoich preferencji. \nPrzed toba kilkanascie pytan - jesli twoja odpowiedz na nie bedzie TAK, wpisz w konsole   +   . Jesli bedzie ona rowna nie, wpisz   -   . \nMilego quizowania!")
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
run_away=  0
cant_you_see_me=0
blue_hour= 0
lovesong= 0
magic= 0
gbgb= 0
srr= 0
ctf= 0
LEveL= 0

print("1. Pytania o twoj ULUBIONY nastroj piosenek")
odp_gr= input("Czy lubisz wesole, pozytywnie brzmiace piosenki?")
if odp_gr == "+":
    piosenki={
        "CROWN": +1,
        "Blue Hour": +1,
        "0X1=Lovesobg (I Know I love You)": +1,
        "Magic": +1,
        "Sugar Rush Ride": +1,
        "Chasing that feeling": +1,
        "LEveL": +1
    }
elif   odp_gr == "-":
    odp_gr= input("Czy lubisz piosenki piosenki dajace vibe bad boy/girl?")
    if odp_gr == "+":
        piosenki={
            "Good Boy Gone Bad": +1
        }
    elif odp_gr == "-":
        odp_gr= input("Czy lubisz piosenki o mniej pozytywnym nastroju?")
        if odp_gr == "+":
            piosenki={
                "9 and Three Quarters (Run Away)":  +1,
                "Can't You See Me?":+1,
            }
   
print(piosenki.keys())
print(piosenki.values())



