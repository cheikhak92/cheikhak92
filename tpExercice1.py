def NbCMin(phrase):
    nbCaMinTrouve=0
    for c in phrase:
        if 'a' <= c <= 'z':
            nbCaMinTrouve += 1
    return nbCaMinTrouve

def NbCMaj(phrase):
    nbCaMajTrouve=0
    for c in phrase:
        if 'A' <= c <= 'Z':
            nbCaMajTrouve += 1
    return nbCaMajTrouve

def NbCAlpha(phrase):
    nbCaAlphaTrouve=0
    for c in phrase:
        if c < 'A'or 'Z' < c < 'a'or c > 'z' :
            nbCaAlphaTrouve += 1            
    return nbCaAlphaTrouve

def LongMaj(phrase):
    longSecTrouve=0
    longSecActu=0
    for c in phrase:
        if('A' <= c <= 'Z'):
            longSecActu += 1
            if longSecActu > longSecTrouve:
               longSecTrouve = longSecActu
        else:
            longSecActu =0
    return longSecTrouve

def LongMin(phrase):
    longSecTrouve=0
    longSecActu=0
    for c in phrase:
        if('a' <= c <= 'z'):
            longSecActu += 1
            if longSecActu > longSecTrouve:
               longSecTrouve = longSecActu
        else:
            longSecActu =0
    return longSecTrouve
def affichage():
    longTotal = 0
    for c in phrase:
        longTotal += 1
    print("Le nombre total de caracteres =",longTotal)
    print("Le nombre de lettres majuscules =",NbCMaj(phrase))
    print("Le nombre de lettres minuscules =",NbCMin(phrase))
    print("Le nombre de caracteres non alphabetique=",NbCAlpha(phrase))
    print("La longeur de la plus longue sequence de lettres minuscules=",LongMin(phrase))
    print("La longeur de la plus longue sequence de lettres majuscules=",LongMaj(phrase))
    
def Score(phrase):
    longTotal = 0
    for c in phrase:
        longTotal += 1    
    score=longTotal*4+(longTotal-NbCMaj(phrase))*2+(longTotal-NbCMin(phrase))*3+NbCAlpha(phrase)*5-(LongMaj(phrase)*2+LongMin(phrase)*2)
    return score
def jugement():
    score=Score(phrase)
    if score < 20:
        print("tres faible")
    elif 20 < score < 40:
        print("faible")
    elif 40 < score < 80:
        print("fort")
    else:
        print("tres fort")
    
phrase=input("Entrer votre phrase:")
affichage()
print("le score du mot de pass=",Score(phrase))
jugement()






