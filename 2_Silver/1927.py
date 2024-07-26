# https://acmicpc.net/problem/1927
import heapq , sys
input = sys.stdin.readline

arr = []                        # default 최소 힙

n = int(input())

for _ in range(n) :
  x = int(input())
  if x > 0 :
    heapq.heappush(arr,x)

  else :
    if len(arr) == 0 :          # heap이 없을 때
      print(0)
    else :
      print(heapq.heappop(arr))


# 37044	128