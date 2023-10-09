import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
d_increase = [1] * 1001
d_decrease = [1] * 1001

for i in range(1,n) :
    for j in range(0,i) :
        if a[i] > a[j] :
            d_increase[i] = max(d_increase[i],d_increase[j]+1)

for i in range(n-1,-1,-1) :
    for j in range(n-1,i,-1) :
        if a[i] > a[j] :
            d_decrease[i] = max(d_decrease[i],d_decrease[j]+1)

result = []
for i in range(n) :
    result.append(d_increase[i] + d_decrease[i] - 1)
    
print(max(result))