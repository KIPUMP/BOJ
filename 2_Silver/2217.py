import sys
input = sys.stdin.readline
N = int(input())

loaf = []
result = []

for _ in range(N) :
  max_weight = int(input())
  loaf.append(max_weight)

loaf.sort(reverse=True)

for i in range(1,N+1) :
  result.append(loaf[i-1] * i)

print(max(result))