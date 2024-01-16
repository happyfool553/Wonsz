import random
'''listaGotowa to lista z liczbami wybranymi przez bota'''
wylosowanaLiczba = -1
listaGotowa = [0,0,0,0,0,0,0]

def losowanieLiczby(listaGotowa):
    numerListy = 0
    while numerListy <7:
        wylosowanaLiczba = random.randint(1,49)
        listaGotowa[numerListy] = wylosowanaLiczba
        numerListy= numerListy+1
    return listaGotowa



losowanieLiczby(listaGotowa) 
print (listaGotowa)   
