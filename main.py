
def circleGraph(n):
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

print(circleGraph(15))
