# https://www.acmicpc.net/problem/14719

def find_max_value(start,end) :
    max_val = arr[start]
    
    for i in range(start,end) :
        if arr[i] > max_val :
            max_val = arr[i]
            
    return max_val
    

h,w = map(int,input().split())
arr = list(map(int,input().split()))


result = 0

for i in range(w) : 
    left_top = find_max_value(0,i)
    right_top = find_max_value(i,w)
    
    if left_top > 0 and right_top > 0 :
        if left_top > right_top :
            if right_top - arr[i] > 0 :
                result += right_top - arr[i]
        
        else :
            if left_top - arr[i] > 0 :
                result += left_top - arr[i]
            
print(result)
    
# 맞았습니다!!	31120	40