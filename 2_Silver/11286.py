import heapq,sys
input = sys.stdin.readline
abs_heap = []

for _ in range(int(input())) :
    num = int(input())
    if num :
        heapq.heappush(abs_heap,(abs(num),num))
    else :
        if abs_heap :
            print(heapq.heappop(abs_heap)[1])
        else :
            print(0)