import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def factorial(n) :
  if n == 1 :
    return 1
  else :
    return n * factorial(n-1)

for _ in range(int(input())) :
  N,M = map(int,input().split())
  if N == M :
    print(1)
  else :
    print(factorial(M)//(factorial(N) * factorial(M-N)))



