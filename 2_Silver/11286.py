import heapq, sys
input = sys.stdin.readline
arr = []

for _ in range(int(input())) :
    n = int(input())

    if n :
        heapq.heappush(arr,(abs(n),n))
    else :
        if arr :
            y = (heapq.heappop(arr)[1])
            print(y)
        else :
            print(0)

