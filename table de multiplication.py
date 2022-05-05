print("\t---Table de multiplication d'un entier saisi---")
n = int(input("\tEntrer le nombre entier pour la table:"))

print("\tTable de multilication de",n)
for i in range(13):
    print(n,"x",i,"=",(n*i))

print("\tTable de multiplication des nombre pairs jusqu'à",n,"si",n,"est pair ou jusqu'à",(n-1),"si",n,"est impair")
for i in range(2,n+1,2):
    print("\tTable de multiplication de",i)
    for j in range(13):
        print(i,"x",j,"=",(j*i))

print("\tTriangle d'étoile")
for i in range(n+1):
    print(i*"*")

print("\tTriangle de Pascale")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    

print("\tTriangle de Pascale")
for i in range(1,n+1):
    for j in range(1,i+1):  
        print(i,end=" ")
    print()

print("\tTriangle de Pascale")
for i in range(n+1):
    for j in range(i+1):
        print((i+j+tmp),end=" ")
    print()




