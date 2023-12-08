from bisect import bisect_left

n = int(input())
a = list(map(int,input().split()))
d = [a[0]]

for i in range(n) :
    if d[-1] < a[i] :
        d.append(a[i])
    else :
        idx = bisect_left(d,a[i])
        d[idx] = a[i]
        
print(len(d))