import random
    
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
