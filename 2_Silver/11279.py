import heapq
import sys
input = sys.stdin.readline
h = []
for _ in range(int(input())) :
  x = int(input())
  if x == 0 :
    if len(h) == 0 :
      print(0)
    else :
      y = -heapq.heappop(h)
      print(y)
  elif x > 0 :
    heapq.heappush(h,x*(-1))