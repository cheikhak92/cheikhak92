print("\t~~~Résolution d'une fonction affine de la forme f(x)=ax+b avec f(x)=0~~~")

print("\t~~~Saisie des paramètres de la fonction~~~")
a = float(input("Entrer la valeur du paramètre a:"))
b = float(input("Entrer la valeur du paramètre b:"))

print("La fonction est f(x)= ",a,"x +",b,"avec f(x)=0")
if a==0 and b==0:
    print("\tPas de solution dans b.")
if a != 0:
    x=b/a
    print("\tLa solution est",x)

print("\tAu revoir et à la prochine")



