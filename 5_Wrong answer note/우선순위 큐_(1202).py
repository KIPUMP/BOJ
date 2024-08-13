# https://www.acmicpc.net/problem/1202
import sys, heapq
input = sys.stdin.readline

n,k = map(int,input().split())

jewelry = [list(map(int,input().split())) for _ in range(n)]    # 보석에 대한 정보
bag = [int(input()) for _ in range(k)]         # 훔친 보석을 담을 가방

jewelry.sort()
bag.sort()

result = 0
h = []

for i in bag :
    while jewelry and jewelry[0][0] <= i :
        heapq.heappush(h, -jewelry[0][1])
        heapq.heappop(jewelry)
        
    if h :
        result -= heapq.heappop(h)
print(result)

# 106008	1880



