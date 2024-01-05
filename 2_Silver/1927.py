import heapq
import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())) :
    x = int(input())
    if x == 0 :
        if len(arr) == 0 :
            print(0)
        else :
            print(heapq.heappop(arr))
            
    else :
        heapq.heappush(arr,x)