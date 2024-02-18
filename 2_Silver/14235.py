import heapq,sys
input = sys.stdin.readline

arr = []

for _ in range(int(input())) :
    a = list(map(int,input().split()))
    
    if a[0] == 0 :
        if len(arr) == 0 :
            print(-1)
        else :
            x = -heapq.heappop(arr)
            print(x)
    else :
        for i in range(1,len(a)) :
            heapq.heappush(arr,-a[i])
            
            
    