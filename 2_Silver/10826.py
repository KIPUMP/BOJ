n = int(input())
d = [0] * (10001)

d[1] = 1
d[2] = 1

if n <= 2 :
    print(d[n])
    
else :
    for i in range(3,n+1) :
        d[i] = d[i-1] + d[i-2]
    print(d[n])    