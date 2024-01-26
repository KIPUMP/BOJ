k,n = map(int,input().split())
lines = [int(input()) for _ in range(k)]
start, end = 1, max(lines)
mid = (start + end) // 2

def get_total(t) :
    result = 0
    for l in lines :
        if l >= t :
            result += l // t    
    return result

while start <= end :
    if get_total(mid) >= n :
        result = mid 
        start = mid + 1
        
    else :
        end = mid - 1
        
    mid = (start + end) // 2
    
print(result)
        
    