n = int(input())
budget = list(map(int,input().split()))
m = int(input())

start, end = 1 , max(budget)
mid = (start + end) // 2

def get_total(x) :
    result = 0
    for b in budget :
        if b <= x :
            result += b
        else :
            result += x
            
    return result

x = 0
while start <= end :
    if get_total(mid) > m : 
        end = mid - 1
        
    else :
        x = mid
        start = mid + 1
        
    mid = (start + end) // 2
        
print(x)



    
    