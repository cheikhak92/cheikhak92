def exercice1():
    entier=int(input("saisie un entier(positif):"))#declaration d'une variable entier saisir un nombre entier
    entierTrouve = True
    #if(len(str(entier))==5):verifier si un entier est composé de 5 chiffres
    if(entier > 0):
        nombre=str(entier)
        for chiffre in nombre:
            if nombre.count(chiffre)>1:
                entierTrouve = False
                break
        if entierTrouve == True:
            print("l'entier saisie est distincts")
        else:
            print("l'entier saisie n'est pas distincts")        
    else:
        print("Saisir un entier positif")

def exercice2():
    print("----Voici les nombres qui vérifient la condition----")
    entier = 0
    while(1):
        if(len(str(entier))==3) and (entier > 0):
            nombre=str(entier)
            chiffre0=int(nombre[0])
            chiffre1=int(nombre[1])
            chiffre2=int(nombre[2])
            som = chiffre0 + chiffre1 + chiffre2
            prod = chiffre0 * chiffre1 * chiffre2
            if prod % som ==0:
                print(entier)
        entier+=1            
exercice2()      
