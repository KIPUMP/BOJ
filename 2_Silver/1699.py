n = int(input())
d = [i for i in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,i) :
        if j**2 > i :
            break
        else :
            if d[i] > d[i - (j**2)] + 1:
                d[i] = d[i - (j**2)] + 1
                
print(d[n])