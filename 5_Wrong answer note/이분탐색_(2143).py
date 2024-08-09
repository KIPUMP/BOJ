from bisect import bisect_left, bisect_right

t = int(input())
n = int(input())
a = list(map(int,input().split()))
sum_a = []

for i in range(n) :                # 리스트 a의 부분합
    s = a[i]
    sum_a.append(a[i])
    for j in range(i+1,n) :
        s += a[j]
        sum_a.append(s)
    
m = int(input())
b = list(map(int,input().split()))    
sum_b = []

for i in range(m) :                  # 리스트 b의 부분합
    s = b[i]
    sum_b.append(s)
    for j in range(i+1,m) :
        s += b[j]
        sum_b.append(s)

sum_a.sort()                        # bisect를 사용할 때는 무조건 리스트를 정렬해야 한다.
sum_b.sort()

result = 0

for i in range(len(sum_a)) :
    l = bisect_left(sum_b , t-sum_a[i])
    r = bisect_right(sum_b , t-sum_a[i])
    result += r-l
    
print(result)

#  71952	864