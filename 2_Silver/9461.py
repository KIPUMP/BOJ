import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
d = [0] * 101
def surf(n) :
  if n <= 3 :
    return 1
  
  if d[n] != 0:
    return d[n]

  d[n] = surf(n-2) + surf(n-3)
  return d[n]


for i in range(int(input())) :
  n = int(input())  
  print(surf(n))
