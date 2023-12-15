n = int(input())
liquid = sorted(map(int,input().split()))
start ,end = 0 , n-1
mixed = liquid[start] + liquid[end]
result = [liquid[start],liquid[end]]

while start < end:
    sum_val = liquid[start] + liquid[end]
    
    if abs(mixed) > abs(sum_val) :
        mixed = abs(sum_val)
        result = [liquid[start],liquid[end]]
        if mixed == 0 :
            break
        
    if sum_val < 0 :
        start += 1
        
    else :
        end -= 1        
    

print(*result)