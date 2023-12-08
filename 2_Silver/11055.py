n = int(input())
a = list(map(int,input().split()))
d = a[:]

for i in range(n) :
    for j in range(i) :
        if a[i] > a[j] :
            d[i] = max(d[i],d[j] + a[i])

print(max(d))