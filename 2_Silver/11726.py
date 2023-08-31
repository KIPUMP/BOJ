import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
d = [0] * 1001

def area(n) :
  if n <= 2 :
    return n
  if d[n] != 0 :
    return d[n]
  
  d[n] = (area(n-2) + area(n-1)) % 10007
  return d[n]

n = int(input())
print(area(n))
