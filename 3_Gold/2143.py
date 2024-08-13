# https://www.acmicpc.net/problem/2143
from bisect import bisect_left,bisect_right

t = int(input())                    # a,b 부분배열의 합이 T가 되어야 됨
n = int(input())                
a = list(map(int,input().split()))
sum_a = []                          # a 부분배열의 합을 구할 리스트
for i in range(n) :
    s = a[i]
    sum_a.append(s)
    for j in range(i+1,n) :
        s += a[j]
        sum_a.append(s)

m = int(input())
b = list(map(int,input().split()))
sum_b = []                          # b 부분배열의 합을 구할 리스트
for i in range(m) :
    s = b[i]
    sum_b.append(s)
    for j in range(i+1,m) :
        s += b[j]
        sum_b.append(s)
        
sum_a.sort()                        # 정렬
sum_b.sort()
result = 0

for i in range(len(sum_a)) :
    l = bisect_left(sum_b,t-sum_a[i])
    r = bisect_right(sum_b,t-sum_a[i])
    
    result += r-l
    
print(result)
 