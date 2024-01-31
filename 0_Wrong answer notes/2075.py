import sys,heapq
input = sys.stdin.readline

arr = []
heapq.heapify(arr)
n = int(input())

for _ in range(n) :
    new_list = list(map(int,input().split()))

    for i in range(n) :
        if len(arr) < n :
            heapq.heappush(arr,new_list[i])
        
        else :
            if arr[0] < new_list[i] :
                heapq.heappop(arr)
                heapq.heappush(arr,new_list[i])
            
print(arr[0])
