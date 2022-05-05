def BmiFonction():
    a=input("\tSaisir le sex(M = 1 ou F = 2) 1 ou 2 svp:")
    b=int(input("\tSaisir la taille en cm svp:"))
    c=int(input("\tSaisir le poids en kg svp:"))
    if(a == 1):
        PI= (b-100)-(b-150)/4
    else:
        PI= (b-100)-(b-120)/4
    print("PI =",PI)

    BMI = c/(pow((b/100),2))
    print("BMI =",BMI)
    if(BMI < 27):
        print("\tNormale")
    elif(BMI >= 27) and (BMI < 32):
        print("\tobèse")        
    elif(BMI >= 32):
        print("\Malade")        

def PupilleFonction():
    a=int(input("\tSaisir l'age:"))
    if(a >= 6) and (a <= 7):
        print("\tPoussin")
    elif(a >= 8) and (a <= 9):
        print("\tPupille")
    elif(a >= 10) and (a <= 11):
        print("\tMinime")
    elif(a >= 12) and (a <= 17):
        print("\Cadet")        
    elif(a > 17):
        print("\Adulte")        

BmiFonction()
PupilleFonction()
