# https://www.acmicpc.net/problem/17266

n = int(input())
m = int(input())
lamp = list(map(int,input().split()))

left = 1
right = n
result = 0

while left <= right :
    mid = (left + right) // 2
    token = True
    
    if lamp[0] - mid > 0 :
        token = False
        
    for i in range(1,m) :
        if lamp[i] - lamp[i-1] > 2 * mid :
            token  = False
            break
        
    if n - lamp[-1] > mid :
        token = False
        
    if token :
        result = mid 
        right = mid - 1
        
    else :
        left = mid + 1
        
print(result)


# 42036	320