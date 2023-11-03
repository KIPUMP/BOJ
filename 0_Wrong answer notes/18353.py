n = int(input())
soldier = list(map(int,input().split()))
d = [1] * n
for i in range(n) :
    for j in range(i) :
        if soldier[i] < soldier[j] :
            d[i] = max(d[i],d[j] + 1)

print(n-max(d))