import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
d = [0] * 1001

def area(n) :
  if n <= 1 :
    return 1
  if d[n] != 0 :
    return d[n]

  d[n] = (area(n-1) + (2 * area(n-2))) % 10007

  return d[n]

n = int(input())
print(area(n))