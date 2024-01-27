n,m = map(int,input().split())
times = list(map(int,input().split()))

start = max(times)
end = sum(times)
result = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    cnt = 1
    
    for t in times :
        if total + t > mid :
            cnt += 1
            total = 0
            
        total += t
        
    if cnt <= m :
        result = mid
        end = mid - 1
        
    else :
        start = mid + 1
        
print(result)