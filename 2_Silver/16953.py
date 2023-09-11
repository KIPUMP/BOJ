import sys
import heapq
input = sys.stdin.readline
A, B = map(int, input().split())

def choice_one(cnt,a) :
  return cnt+1, a * 2

def choice_two(cnt,a) :
  return cnt+1 , a * 10 + 1
  
def solution(a,b) :
  q = [(0,a)]
  while q :
    cnt,a = heapq.heappop(q)
    if a == b :
      return cnt+1
    elif  a < b :
      heapq.heappush(q,choice_one(cnt,a))
      heapq.heappush(q,choice_two(cnt,a))
  return -1

print(solution(A,B))