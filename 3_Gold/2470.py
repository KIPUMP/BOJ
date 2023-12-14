n = int(input())
liquid = sorted(map(int,input().split()))
left,right = 0,1

def binary_search(target) :
    
    start = 0
    end = n - 1
    while start <= end : 

        mid = (start + end) // 2
        
        if liquid[mid] == target :
            return mid
        
        elif liquid[mid] < target :
            start = mid + 1
            
        else :
            end = mid - 1
            
result = [[0] * n for _ in range(n)]
while left <= right and right <= n :    
    result.append((liquid[left],liquid[right]))
    
    