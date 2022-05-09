import math

print("\t~~~Résolution d'une fonction affine de la forme f(x)=ax^2+bx+c avec f(x)=0~~~")
a = float(input("Entrer la valeur du paramètre a:"))
b = float(input("Entrer la valeur du paramètre b:"))
c = float(input("Entrer la valeur du paramètre c:"))

if a != 0:
    print("La fonction est la forme f(x)= ",a,"x^2 +",b,"x +",c,"avec f(x)=0")
    delta = pow(b,2)-4*a*c
    if delta < 0:
        print("\tPas de solution dans IR")
    if delta == 0:
        print("\tLa fonction a une solution double")        
        x = (-b/2*a)
        print("\tLa solution double est x =",x)
    else:
        print("\tLa fonction admet deux solution distinctes")
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("\tLes deux solutions sont",x1,"et ",x2)

else:
    print("\tLa fonction n'est pas de 2nd degrée")
