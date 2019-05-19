from random import randint

def cycleGraph(n):
    t = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        if i == 0:
            t[i].pop(i+1)
            t[i].insert(i+1, 1)

            t[i].pop(i-1)
            t[i].insert(n, 1)
        elif i == n-1:
            t[i].pop(0)
            t[i].insert(0, 1)

            t[i].pop(i-1)
            t[i].insert(i-1, 1)
        else:
            t[i].pop(i+1)
            t[i].insert(i+1, 1)

            t[i].pop(i-1)
            t[i].insert(i-1, 1)
    return t

def saturation(t):
    b = 0
    for i in t:
        b += i.count(1)
    fullSaturation = (len(t)*(len(t)-1)/2)
    return ((b/2)/fullSaturation)*100

def transposition(t):
    t1 = []
    for i in range(len(t)):
        t2 = []
        for j in range(len(t)):
            t2.append(t[j][i])
        t1.append(t2)
    return t1

def isEuler(t):
    a = t[:]
    b = transposition(t)
    for i in a:
        i = list(filter(lambda x: x==1, i))
        if len(i) % 2 != 0:
            return False
    for i in b:
        i = list(filter(lambda x: x==1, i))
        if len(i) % 2 != 0:
            return False
    return True

def setSaturation(t, n):

    while(saturation(t) < n):
        for i in range(len(t)):
            for j in range(len(t)//2):
                if saturation(t) < n:
                    if t[i][j] == 0 and i != j:
                        k = randint(j, len(t)-1)
                        if j != k and i != k and t[i][k] == 0 and t[j][k] == 0:
                            t[i][j] = 1
                            t[j][i] = 1

                            t[i][k] = 1
                            t[k][i] = 1

                            t[k][j] = 1
                            t[j][k] = 1

                        if saturation(t) > n:
                            break

t = cycleGraph(50)
print(isEuler(t))
setSaturation(t, 30)

for i in t:
    print(i, i.count(1))

print(f'{saturation(t)}%, is Euler: {isEuler(t)}')
