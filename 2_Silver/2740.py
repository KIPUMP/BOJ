import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [[0] * m for _ in range(n)]

for i in range(n) :
  arr = list(map(int,input().split()))
  for j in range(m) :
    a[i][j] = arr[j]

m,k= map(int,input().split())
b = [[0] * k for _ in range(m)]

for i in range(m) :
  arr = list(map(int,input().split()))
  for j in range(k) :
    b[i][j] = arr[j]

result = [[0] * k for _ in range(n)]

for i in range(n) :
  for j in range(k) :
    for l in range(m) :
      result[i][j] += a[i][l] * b[l][j]

for i in range(n) :
  for j in range(k) :
    print(result[i][j], end=" ")
  print()

    

