# https://www.acmicpc.net/problem/14235
import sys,heapq
input = sys.stdin.readline
arr = []


n = int(input())
for _ in range(n) :
  a = list(map(int,input().split()))
  if a[0] == 0 :
    if len(arr) == 0 :              # 길이가 0 이면 -1 출력
      print(-1)
    else :
      print(-heapq.heappop(arr))    # 최대힙 출력
  else :
    gift = a[1:]                    # 거점지 배열
    for i in range(a[0]) :        
      heapq.heappush(arr,-gift[i])  # 최대 힙 삽입


# 40920	128