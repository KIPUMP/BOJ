import heapq
n = int(input())

result = []
for _ in range(n) :
    arr = list(map(int,input().split()))
    for i in range(n) :
        if len(result) < n :
            heapq.heappush(result,arr[i])
        else :
            if result[0] < arr[i] :
                heapq.heappop(result)
                heapq.heappush(result,arr[i])
    
print(result[0])
    


    

        
        
    
