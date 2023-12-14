n,m = map(int,input().split())
a = list(map(int,input().split()))
left, right = 0,1
result = 0
while left <= right and right <= n :
    total = sum(a[left : right])
    
    if total == m :
        result += 1
        right += 1
        left += 1
        
    elif total > m :
        left += 1
        
    else :
        right += 1
        
print(result)