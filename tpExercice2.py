import random


def deplacer(T, K):

    for i in range(50):
        a=random.randint(0,100)
        if a == K:
            a=random.randint(0,100)
        else:
            T.append(a)
    print(T)
    n=0
    m=49
    for i in T:
       if i < K:
           tmp = T[n]
           T[n] = i
           i = tmp
           n += 1
       elif a > K:
           tmp = T[m]
           T[m] = i
           i = tmp
           m = m-1
    print(T)

K=int(input("Donner la valeur de K(entre 0 et 100):"))
T = []
print(deplacer(T, K))
