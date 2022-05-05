import random

print("\t=====Exemple de fonction======")

def saisirEntier():
    a = int(input("\tEntrer un nombre"))
    return a

def table(n):
    print("\tTable de mul tiplication")
    for i in range(13):
        print(n,"x",i,"=",(n*i))

def premier(x):
    cpt = 0
    for i in range(1,x+1):
        if x%i==0:
            cpt += 1
    if cpt ==2:
        print(x,"\test un nombre premier")
    else:
        print(x,"\tn'est pas un nombre premier")
def premier1(x):
    cpt = 0
    for i in range(2,(x/2)+1):
        if x%i==0:
            cpt += 1
    if cpt ==0:
        print(x,"\test un nombre premier")
    else:
        print(x,"\tn'est pas un nombre premier")
def premier2(x):
    i=2
    while(i <= (n/2)) and n%i != 0:
        i+=1
    if (i > n/2):
        print(x,"\test un nombre premier")
    else:
        print(x,"\tn'est pas un nombre premier")

def carré(x):
    ok=0
    for i in range(1,x+1):
        if (x%i==0 and i*i == x):
            ok=1
    if ok==1:
            print(x,"\test un nombre carré")
    else:
            print(x,"\tn'est pas un nombre carré")
        
def parfait(x):
    cumul = 0
    for i in range(1,x):
        if x%i == 0:
            cumul += i
    if cumul == x:
        print(x,"\test un nombre parfait")
    else:
        print(x,"\tn'est pas un nombre parfait")

def saisirNombreAuHasard(x):
    cpt = 0
    a=random.randint(0,11)
    print("a=",a)
    b=int(input("\tSaisir un nobre au hasard svp:"))
    while a != b and cpt != 4:
        if(b < a):
            print("\tTrès petit")
        else:
            print("\tTrès grand")        
        cpt +=1
        c=(5-cpt)
        if c != 1:
            print("\tIl vous reste",c,"tentatives")
        else:
            print("\tIl vous reste",c,"seule tentatives")        
        b=int(input("\tSaisir de nouveau un nombre au hasard svp:"))

    if a == b:
        print("\tTu as trouvé la bonne valeur")
        print("\tBravoo tu as gagné")

    if(cpt == 4):
        print("\tTu as atteint le nombre de tentatives permis")
        print("\tDonc tu as perdu")
def menu():
    print("\t====1:saisirEntier.======")
    print("\t====2:table.======")
    print("\t====3:premier.======")
    print("\t====4:Quitter.======")
    print("\t=====Faites votre choix.======")

    x = saisirEntier()
    if x == 1:
        A = saisirEntier()
    elif x == 2:
        A = saisirEntier()
        table(A)
    elif x ==3:
        A = saisirEntier()
        premier(A)
    elif x == 4:
        return

#A = saisirEntier()
menu()
    

#carré(A)
#parfait(A)
#saisirNombreAuHasard(A)
